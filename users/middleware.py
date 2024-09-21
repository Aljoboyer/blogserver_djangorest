# from rest_framework_simplejwt.tokens import AccessToken
# from django.core.exceptions import ObjectDoesNotExist
# from .models import User
# from django.http import JsonResponse
# from urllib.parse import urlparse

# class JWTAuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.public_paths = [
#             '/user/login/',   # Public login API
#             '/user/register/',  # Public register API
#         ]

#     def __call__(self, request):
#         # Check if the request path is in public paths
#         parsed_url = urlparse(request.path).path
#         if parsed_url in self.public_paths:
#             return self.get_response(request)  # Skip JWT check for public paths

#         # If the path is not public, check for JWT token in the Authorization header
#         auth_header = request.headers.get('Authorization')
        
#         if auth_header:
#             try:
#                 token_type, token = auth_header.split(' ')
#                 if token_type.lower() == 'bearer':
#                     access_token = AccessToken(token)
#                     user_id = access_token['user_id']  # Should be UUID string in the token payload

#                     try:
#                         # Fetch user by UUID
#                         user = User.objects.get(id=user_id)
#                         request.user = user  # Attach the user to the request

#                     except ObjectDoesNotExist:
#                         return JsonResponse({'error': 'User not found'}, status=404)

#                 else:
#                     return JsonResponse({'error': 'Authorization header must start with Bearer'}, status=401)
#             except ValueError:
#                 return JsonResponse({'error': 'Invalid Authorization header format'}, status=400)
        
#         else:
#             return JsonResponse({'error': 'Authorization header missing'}, status=401)

#         # Proceed with the request if token is valid
#         response = self.get_response(request)
#         return response
