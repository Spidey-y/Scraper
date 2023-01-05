from rest_framework.decorators import api_view, permission_classes
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from logs.models import Log

class RegisterUserView(generics.GenericAPIView):
    """
    Signup a new user, returns the user instant with bearer key, status 201
    status 400 if the data is invalid
    """
    permission_classes = ()
    serializer_class = UserRegisterSerializer
    def post(self, request):
        user = UserRegisterSerializer(data=request.data)
        if user.is_valid():
            user.save()
            user = User.objects.get(id=user.data["id"])
            token = Token.objects.create(user=user)
            return Response({"Token": token.key}, status=status.HTTP_201_CREATED)
        return Response({"details": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """
    Login a new user, returns bearer and sets cookie to jwt token, status 200
    status 404 if the user doesnt exist, or email or password incorrect
    status 400 if the data is invalid
    """
    serializer_class = UserLoginSerializer
    permission_classes = ()
    def post(self, request):
        tmp = self.serializer_class(data=request.data)
        if tmp.is_valid():
            try:
                user = User.objects.get(email=tmp.data['email'])
                if user and user.check_password(raw_password=tmp.data['password']):
                    log = Log(action="Logged in", user=user)
                    log.save()
                    token = ""
                    try:
                        token = Token.objects.create(user=user)
                    except:
                        token = Token.objects.get(user_id=user.id)
                    return Response({"Token": token.key}, status=200)
                return Response({"details": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
            except:
                return Response({"details": "Invalid credentials"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"details": "Invalid data"},status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST',)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def LogoutView(request):
    """
    User logout, status 200 returned
    Returns invalid token if token is not found (user signed out)
    """
    log = Log(action="Logged out", user=request.user)
    log.save()
    request.user.auth_token.delete()
    return Response({"details": "User Logged out successfully"}, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ProfileView(request):
    """
    Get user profile, must provide 'Token {token}' in 'Authorization' header
    """
    try:
        user = request.user
    except:
        return Response(data="UNAUTHORIZED".lower(),status=status.HTTP_401_UNAUTHORIZED)
    serializer = UserRegisterSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
