import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}.'

    def condition_description(self):
        if self.condition == 5:
            return "Like new!"
        elif self.condition >= 4:
            return "Gently used"
        elif self.condition >= 3:
            return "Used with care"
        elif self.condition >= 2:
            return "A bit rough"
        elif self.condition >= 1:
            return "Heavily worn"
        else:
            return "Really bad"