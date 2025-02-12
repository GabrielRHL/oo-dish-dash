from models.menu.menu import Menu

class Dish(Menu):
    def __init__(self, name, price, description):
        super().__item__(name, price)
        self._description = description