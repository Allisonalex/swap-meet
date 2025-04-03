class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)

        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False   
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)

            other_vendor.remove(their_item)
            self.add(their_item)

            return True
        
        return False
    
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return False
    
    def swap_by_newest(self, other_vendor):
        
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_newest = min(self.inventory, key=lambda item: item.age)
        other_newest = min(other_vendor.inventory, key=lambda item: item.age)

        return self.swap_items(other_vendor, my_newest, other_newest)