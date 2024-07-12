# users/urls.py

from django.urls import path, include
from .views import UserProfileDetail, AppointmentListCreate, AppointmentDetail

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('profile/', UserProfileDetail.as_view(), name='user-profile'),
    path('appointments/', AppointmentListCreate.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
]
