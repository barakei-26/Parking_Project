from django.db import models
from django.contrib.auth.models import User
from parking_app.models import Slot

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    plate = models.CharField(max_length=15, unique=True, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    slot_reserved = models.ForeignKey(Slot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return f'{self.slot_reserved} reserved from {self.arrival_time} to {self.leave_time} by {self.user}'