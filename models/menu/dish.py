from models.menu.menu import Menu

class Dish(Menu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description

    def __str__(self):
        return self._name