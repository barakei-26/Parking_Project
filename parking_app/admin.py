from django.contrib import admin
from parking_app.models import Building, Floor, Slot 

# Register your models here.
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Slot)
