from django.urls import path, include
from allauth.account.views import LoginView, SignupView
from .views import UserProfileDetail, AppointmentListCreate, AppointmentDetail, profile, dashboard

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('appointments/', AppointmentListCreate.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('register/', SignupView.as_view(template_name='account/signup.html'), name='register'),
]
