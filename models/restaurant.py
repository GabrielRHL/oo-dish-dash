from models.rating import Rating
from models.menu.menu import Menu
from models.menu.dish import Dish
from models.menu.drink import Drink

class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._active = False
        self._rate = []
        self._menu = []
        Restaurant.restaurants.append(self)

    @property
    def active(self):
        return 'Ativo' if self._active else 'Desativado'

    def __str__(self):
        return f'{self._name} | {self._category}'
    
    def change_state(self):
        self._active = not self._active

    def receive_rate(self, client, rate):
        if 0 < rate <= 5:
            rate = Rating(client, rate)
            self._rate.append(rate)

    @property
    def rate_avg(self):
        if not self._rate:
            return '-'
        rate_sum = sum(rate._rate for rate in self._rate)
        rating_qtd = len(self._rate)
        avg = round(rate_sum / rating_qtd, 1)
        return avg
    
    def add_to_menu(self, item):
        if isinstance(item, Menu):
            self._menu.append(item)

    @property
    def display_menu(self):
        print(f'Cardápio do restaurante {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            if isinstance(item, Dish):
                dish_message = f'{i}. Nome do prato: {item._name} | Preço: R${item._price} | Descrição: {item._description}'
                print(dish_message)
            elif isinstance(item, Drink):
                drink_message = f'{i}. Nome da bebida: {item._name} | Preço: R${item._price} | Tamanho: {item._size}'
                print(drink_message)

    
    @classmethod
    def display_restaurants(cls):
        print(f'{'Restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Status'.ljust(15)} | {'Avaliação'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(15)} | {restaurant._category.ljust(15)} | {restaurant.active.ljust(15)} | {restaurant.rate_avg}')