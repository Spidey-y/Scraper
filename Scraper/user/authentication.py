from config import JWT_SECRET
from rest_framework import authentication, exceptions
import jwt
from .models import User
import datetime

class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")
        print(datetime.datetime.now())
        if not token:
            return None
        # try:
        print(JWT_SECRET, token)
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        # except:
        #     raise exceptions.AuthenticationFailed("Unauthorized")
        user = User.objects.get(id=payload["id"])
        return (user, None)
