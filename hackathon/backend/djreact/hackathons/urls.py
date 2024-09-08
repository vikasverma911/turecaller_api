from django.urls import path
from .views import HackathonList, HackathonDetail, HackathonSubmissionList, HackathonSubmissionDetail

urlpatterns = [
    path('hackathons/', HackathonList.as_view(), name='hackathon_list'),
    path('hackathons/<int:pk>/', HackathonDetail.as_view(), name='hackathon_detail'),
    path('hackathon-submissions/', HackathonSubmissionList.as_view(), name='hackathon-submission-list'),
    path('hackathon-submissions/<int:pk>/', HackathonSubmissionDetail.as_view(), name='hackathon-submission-detail'),
]
