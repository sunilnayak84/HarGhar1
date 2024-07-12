from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the home app URLs
    path('api/', include('users.urls')),
    path('accounts/', include('allauth.urls')),  # Add this line to handle accounts URLs
]
