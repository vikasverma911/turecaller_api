from rest_framework import generics
from .serializers import HackathonSerializer, HackathonSubmissionSerializer
from .models import Hackathon, HackathonSubmission


class HackathonList(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class HackathonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class HackathonSubmissionList(generics.ListCreateAPIView):
    queryset = HackathonSubmission.objects.all()
    serializer_class = HackathonSubmissionSerializer


class HackathonSubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HackathonSubmission.objects.all()
    serializer_class = HackathonSubmissionSerializer
