from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, ContactSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User, Contact
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            try:
                validate_password(password)
            except ValidationError as e:
                return Response({"Error": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST)
                
            if password:
                user = serializer.save()
                user.set_password(password)
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
            return Response({"Error": "Password required"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((AllowAny,))
class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ =Token.objects.get_or_create(user = user)
            return Response( {"Token":token.key },status=status.HTTP_200_OK )
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class MarkSpamView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        
        if not phone_number:
            return Response({"detail": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        user_updated = User.objects.filter(phone_number=phone_number).update(is_spam=True)
        contact_updated = Contact.objects.filter(phone_number=phone_number).update(is_spam=True)

        if not user_updated and not contact_updated:
            return Response({"detail": "Phone number not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"detail": "Phone number marked as spam"}, status=status.HTTP_200_OK)


class SearchByNameView(APIView):
    def get(self, request):
        query = request.query_params.get('name', '').strip()
        
        if not query:
            return Response({"detail": "Name query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Search for usernames starting with and containing the query
        users_start_with = User.objects.filter(username__istartswith=query).values('username', 'phone_number', 'is_spam')
        users_contains = User.objects.filter(username__icontains=query).exclude(username__istartswith=query).values('username', 'phone_number', 'is_spam')

        # Search for names starting with and containing the query
        contacts_start_with = Contact.objects.filter(name__istartswith=query).values('name', 'phone_number', 'is_spam')
        contacts_contains = Contact.objects.filter(name__icontains=query).exclude(name__istartswith=query).values('name', 'phone_number', 'is_spam')

        # Combine results
        results = list(users_start_with) + list(users_contains) + list(contacts_start_with) + list(contacts_contains)

        if not results:
            return Response({"detail": "No results found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(results, status=status.HTTP_200_OK)

class SearchByPhoneNumberView(APIView):
    def get(self, request):
        phone_number = request.query_params.get('phone_number', '').strip()
        
        if not phone_number:
            return Response({"detail": "Phone number query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a registered user exists with the given phone number
        user = User.objects.filter(phone_number=phone_number).first()

        if user:
            return Response({
                "name": user.username,
                "phone_number": user.phone_number,
                "is_spam": user.is_spam,
                "registered_user": True
            }, status=status.HTTP_200_OK)

        # If no registered user, check in the Contact model
        contacts = Contact.objects.filter(phone_number=phone_number).values('name', 'phone_number', 'is_spam')

        if contacts.exists():
            return Response(list(contacts), status=status.HTTP_200_OK)

        return Response({"detail": "No results found for this phone number"}, status=status.HTTP_404_NOT_FOUND)