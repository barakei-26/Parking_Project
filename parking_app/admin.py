from django.contrib import admin
from parking_app.models import Building, Slot, Floor

# Register your models here.
admin.site.register(Building)
admin.site.register(Slot)
admin.site.register(Floor)
