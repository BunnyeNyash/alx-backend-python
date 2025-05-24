import asyncio
import aiosqlite

# Asynchronous function to fetch all users
async def async_fetch_users():
  async with aiosqlite.connect('users.db') as conn:
    async with conn.cursor() as cursor:
      await cursor.execute("SELECT * FROM users")
      results = await cursor.fetchall()
      return results

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
  async with aiosqlite.connect('users.db') as conn:
    async with conn.cursor() as cursor:
      await cursor.execute("SELECT * FROM users WHERE age > ?", (40,))
      results = await cursor.fetchall()
      return results

# Asynchronous function to run both queries concurrently
async def fetch_concurrently():
  # Use asyncio.gather to run both queries concurrently
  all_users, older_users = await asyncio.gather(
    async_fetch_users(),
    async_fetch_older_users()
  )
  # Return results as a tuple
  return all_users, older_users

if __name__ == "__main__":
    # Run the concurrent fetch and print results
    all_users, older_users = asyncio.run(fetch_concurrently())
    print("All users:", all_users)
    print("Users older than 40:", older_users)
