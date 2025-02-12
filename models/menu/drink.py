from models.menu.menu import Menu

class Drink(Menu):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def __str__(self):
        return self._name