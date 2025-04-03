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
    
    def get_by_category(self, category):
        result = []

        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)

        return result
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)

        if not items_in_category:
            return None
        
        return max(items_in_category, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        for_me_from_other = other_vendor.get_best_by_category(my_priority)
        for_them_from_me = self.get_best_by_category(their_priority)

        if not for_me_from_other or not for_them_from_me:
            return False
        
        return self.swap_items(other_vendor, for_them_from_me, for_me_from_other)

    def swap_by_newest(self, other_vendor):
        
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_newest = min(self.inventory, key=lambda item: item.age)
        other_newest = min(other_vendor.inventory, key=lambda item: item.age)

        return self.swap_items(other_vendor, my_newest, other_newest)
    