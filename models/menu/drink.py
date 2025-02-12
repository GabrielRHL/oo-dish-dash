from models.menu.menu import Menu

class Drink(Menu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description =  description