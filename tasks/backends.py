from .models import *
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken




class EmployerUserJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None
        try:
            token_type, token = auth_header.split()
            if token_type.lower() != 'bearer':
                raise AuthenticationFailed('Invalid token header')
            
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            
            user = Employer.objects.get(id=user_id)
        except Employer.DoesNotExist:
            raise AuthenticationFailed('User does not exist')
        except Exception as e:
            raise AuthenticationFailed('Invalid token')
        
        return (user, token)



class EmployeeUserJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return None
        try:
            token_type, token = auth_header.split()
            if token_type.lower() != 'bearer':
                raise AuthenticationFailed('Invalid token header')
            
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            
            user = Employee.objects.get(id=user_id)
        except Employee.DoesNotExist:
            raise AuthenticationFailed('User does not exist')
        except Exception as e:
            raise AuthenticationFailed('Invalid token')
        
        return (user, token)
