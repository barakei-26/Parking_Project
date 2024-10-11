from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Building, Floor, Slot

class BuildingSerializer(ModelSerializer):
    floors = SerializerMethodField()

    class Meta():
        model = Building
        fields = ['name', 'address', 'floors']

    def get_floors(self, building: Building):
        floors = building.get_floors().all()
        serialized_floors = FloorSerializer(floors, many=True).data
        return serialized_floors

#nested serializers
class FloorSerializer(ModelSerializer):
    slots = SerializerMethodField()

    def get_slots(self, floor: Floor):
        slots = floor.slots.all()
        serialized_slots = SlotSerializer(slots, many=True).data
        return serialized_slots
    
    class Meta():   
        model = Floor
        fields = ['floor_number', 'slots']

class SlotSerializer(ModelSerializer):
    class Meta():
        model = Slot
        fields = ['local_id', 'is_available']

class BuildingResumeSerializer(ModelSerializer):
    number_of_available_slots = SerializerMethodField()
    image_url = SerializerMethodField()

    def get_number_of_available_slots(self, building: Building):
        return building.number_of_available_slots()

    def get_image_url(self, building: Building):
        return f'http://localhost:8000{building.image.url}'

    class Meta(): 
        model = Building
        fields = ['name', 'address', 'image_url', 'number_of_available_slots']
        
