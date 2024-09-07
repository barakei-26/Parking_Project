from django.db import models


# Create your models here.
class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30, unique=True, verbose_name='building address')
    number_of_floors = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    
class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    building =  models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_number = models.SmallIntegerField()
    number_of_spaces = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'floor {self.floor_number} of {self.building}'
    
    class Meta():
        unique_together = [('building','floor_number')]
      
class Slot(models.Model):
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    local_id = models.PositiveSmallIntegerField()
    is_empty =  models.BooleanField(default=True)

    def __str__(self):
        return f'slot {self.local_id} in {self.floor}'
    
    def is_available(self):
        return not self.is_empty

    class Meta():
        verbose_name = 'Parking Slot'
        verbose_name_plural = 'Parking Slots'
        unique_together = [('floor', 'local_id')]




