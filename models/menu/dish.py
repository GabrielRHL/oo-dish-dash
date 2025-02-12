from models.menu.menu import Menu

class Dish(Menu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description

    def __str__(self):
        return self._name
    
    def apply_discount(self):
        self._price -= (self._price * 0.05)