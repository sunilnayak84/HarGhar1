from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .models import Appointment, UserProfile
from .serializers import AppointmentSerializer, UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'user': userprofile})

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
