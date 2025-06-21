# Use official Python 3.10 base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code into the container
COPY . .

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the Django app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "messaging_app.wsgi:application"]
