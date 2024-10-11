from django.db import models
from django.db.models import QuerySet

# Building model
class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=60, unique=True, verbose_name='building address')
    image = models.ImageField(upload_to='building_images/', null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_building = Building.objects.get(pk=self.pk)
            if old_building.image and old_building.image != self.image:
                old_building.image.delete(save=False)
        
        super(Building, self).save(*args, **kwargs)


    # Get all slots associated with this building
    def get_slots(self) -> QuerySet['Slot']:
        return Slot.objects.filter(building=self)
    
    # Get the count of all slots
    def number_of_available_slots(self) -> int:
        return self.get_available_slots().count()
    
    # Get only available slots (is_available=True)
    def get_available_slots(self) -> QuerySet['Slot']:
        return Slot.objects.filter(floor__building=self, is_available=True)
    
    def get_floors(self)->QuerySet['Floor']:
        return Floor.objects.filter(building=self).prefetch_related('slots')

    def number_of_floors(self) -> int:
        return self.get_floors().count()

    
# Floor model
class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, related_name='floors', on_delete=models.CASCADE)
    floor_number = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'floor {self.floor_number} in {self.building}'

    def get_slots(self) -> QuerySet['Slot']:
        return Slot.objects.filter(floor=self)
    
    def number_of_slots(self) -> int:
        return self.get_slots().count()
    
    def available_slots(self) -> QuerySet['Slot']:
        return Slot.objects.filter(floor=self, is_available=True)
    
    def add_slot(self) -> 'Slot':
        local_id=self.number_of_slots()+1
        Slot.objects.create(building=self.building, floor=self, local_id=local_id)

    def populate(self, number_of_slots):
        slots = [Slot(building=self.building, floor=self, local_id=slot_number) for slot_number in range(1,number_of_slots+1)]
        Slot.objects.bulk_create(slots, batch_size=100)

    class Meta:
        unique_together = [('building','floor_number')] 

# Slot model
class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, related_name='slots', on_delete=models.CASCADE)
    local_id = models.PositiveSmallIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Slot {self.local_id} on {self.floor}'

    class Meta:
        unique_together = [('floor', 'local_id')]
        verbose_name = 'Parking Slot'
        verbose_name_plural = 'Parking Slots'
