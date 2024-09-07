import jwt
from django.conf import settings
from django.contrib.auth.models import User
from ninja.security import HttpBearer
from ninja.errors import HttpError

class JWTAuth(HttpBearer):
    def authenticate(self, request, token: str):
        try:
            # Decodifica o token JWT
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_SETTINGS['ALGORITHM']])
            user = User.objects.get(id=payload['user_id'])
            return user
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
            raise HttpError(401, "Invalid or expired token")
