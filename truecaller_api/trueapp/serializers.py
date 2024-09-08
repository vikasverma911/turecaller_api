from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'is_spam']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'is_spam']

class UserDetailSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'contacts']