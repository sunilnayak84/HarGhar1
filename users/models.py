from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('admin', 'Admin')])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(post_save, sender=UserProfile)
def assign_role(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'doctor':
            group, _ = Group.objects.get_or_create(name='Doctors')
            instance.user.groups.add(group)
        elif instance.role == 'admin':
            group, _ = Group.objects.get_or_create(name='Admins')
            instance.user.groups.add(group)
        else:
            group, _ = Group.objects.get_or_create(name='Patients')
            instance.user.groups.add(group)

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='appointments_as_patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='appointments_as_doctor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending')

    def __str__(self):
        return f'Appointment with {self.doctor.username} for {self.patient.username} on {self.date}'
