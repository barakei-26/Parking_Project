from django.contrib import admin
from users.models import Reservation, Profile

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Profile)