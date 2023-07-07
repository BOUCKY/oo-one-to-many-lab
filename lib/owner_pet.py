class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner):
        self.name =name
        self.type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def get_type(self):
        return self._pet_type
    
    def set_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self.type = pet_type
            Pet.all.append(self._pet_type)
        else: 
            raise Exception("Not a valid type of pet.")

    pet_type = property(get_type, set_type)

    def get_owner(self):
        return self._owner
    
    def set_owner(self, owner):
        if owner == Owner:
            self._owner = owner
        else: 
            raise Exception("Object is not of type Owner.")


class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if pet == Pet:
            pet.owner = self
        else: 
            raise Exception("Not a valid type of pet.")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
owner = Owner("Jim")
pet = Pet("Clifford", "dog", owner)
