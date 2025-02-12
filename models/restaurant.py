from models.rating import Rating

class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._active = False
        self._rate = []
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
    
    @classmethod
    def display_restaurants(cls):
        print(f'{'Restaurante'.ljust(15)} | {'Categoria'.ljust(15)} | {'Status'.ljust(15)} | {'Avaliação'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(15)} | {restaurant._category.ljust(15)} | {restaurant.active.ljust(15)} | {restaurant.rate_avg}')