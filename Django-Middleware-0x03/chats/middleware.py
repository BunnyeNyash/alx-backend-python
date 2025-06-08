import logging
from datetime import datetime
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils import timezone

# Configure logging
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(message)s'
)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user (handle anonymous users)
        user = request.user if request.user.is_authenticated else 'Anonymous'
        
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
