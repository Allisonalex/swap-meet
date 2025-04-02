import uuid

class Item:
    def __init__(self, id = None):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__
