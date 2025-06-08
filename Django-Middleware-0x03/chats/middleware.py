import logging
from datetime import datetime, timedelta
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.core.cache import cache
import os

# Configure logging to write to requests.log in project root
log_file = os.path.join(settings.BASE_DIR, 'requests.log')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(message)s',
    filemode='a'  # Append mode to prevent overwriting
)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user (handle anonymous users)
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        
        # Log request information
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current time in server's timezone
        current_hour = timezone.now().hour
        
        # Restrict access between 9PM (21:00) and 6PM (18:00)
        if current_hour >= 21 or current_hour < 18:
            return HttpResponseForbidden("Chat access is restricted outside of 6PM-9PM")
        
        response = self.get_response(request)
        return response

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            # Get client IP
            ip_address = request.META.get('REMOTE_ADDR')
            
            # Cache key for this IP
            cache_key = f"chat_rate_{ip_address}"
            
            # Get current message count and timestamp
            message_data = cache.get(cache_key, {'count': 0, 'timestamp': datetime.now()})
            
            current_time = datetime.now()
            time_diff = current_time - message_data['timestamp']
            
            # Reset count if time window (1 minute) has passed
            if time_diff > timedelta(minutes=1):
                message_data = {'count': 0, 'timestamp': current_time}
            
            # Check message limit (5 messages per minute)
            if message_data['count'] >= 5:
                return HttpResponseForbidden("Message limit exceeded. Please try again later.")
            
            # Increment count
            message_data['count'] += 1
            message_data['timestamp'] = current_time
            cache.set(cache_key, message_data, timeout=60)  # Store for 1 minute
        
        response = self.get_response(request)
        return response

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Authentication required")
        
        # Check if user has admin or moderator role
        # Assuming User model has is_staff or is_superuser for role checks
        if not (request.user.is_staff or request.user.is_superuser):
            return HttpResponseForbidden("Admin or Moderator role required")
        
        response = self.get_response(request)
        return response
