from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from authorizeapp.forms import LoginForm, RegistrationForm
from authorizeapp.models import User
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    form = LoginForm(request.data)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            logger.info(f"User logged in successfully: {user.email}")
            return Response({
                "success": True,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "is_superuser": user.is_superuser,
                    "organization": user.organization,
                    "role": user.role
                }
            })
        logger.warning("Login failed: Invalid credentials")
        return Response({"success": False, "error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({"success": False, "error": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    form = RegistrationForm(request.data)
    if form.is_valid():
        user = form.save()
        logger.info(f"User registered successfully: {user.email}")
        return Response({"success": True, "message": "Registration successful"})
    return Response({"success": False, "error": form.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({"success": True, "message": "Logged out successfully"})