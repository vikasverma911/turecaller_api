from django.urls import path
from .views import (
    RegisterUserView,
    LoginUserView,
    UserDetailView,
    MarkSpamView,
    SearchByNameView,
    SearchByPhoneNumberView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('mark-spam/', MarkSpamView.as_view(), name='mark-spam'),
    path('search-by-name/', SearchByNameView.as_view(), name='search-by-name'),
    path('search-by-phone-number/', SearchByPhoneNumberView.as_view(), name='search-by-phone-number'),
]