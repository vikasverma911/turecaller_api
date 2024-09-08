from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hackathon, HackathonSubmission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class HackathonSubmissionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    hackathon = HackathonSerializer(read_only=True)

    class Meta:
        model = HackathonSubmission
        fields = '__all__'
