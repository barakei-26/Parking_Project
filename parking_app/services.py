from .models import Slot, Building, Floor


##TODO: implement error handling and validation

class BuildingFactory:
    @staticmethod
    def create_building(name, address, number_of_floors):
        return Building.objects.create(name=name, address=address, number_of_floors=number_of_floors)

class FloorFactory:
    @staticmethod
    def create_floor(building, floor_number):
        return Floor.objects.create(building=building, floor_number=floor_number)

class SlotFactory:
    @staticmethod
    def create_slot(floor, local_id): 
        return Slot.objects.create(floor=floor, local_id=local_id)