from models.restaurant import Restaurant
from models.menu.dish import Dish
from models.menu.drink import Drink

restaurant_granu = Restaurant('Granulado', 'Doceria')
restaurant_coco_bambu = Restaurant('Coco Bambu', 'Frutos do mar')
restaurant_il_piacere = Restaurant('Il Piacere', 'Pizzaria')

Restaurant.change_state(restaurant_granu)

# restaurant_granu.receive_rate('Gabriel', 3)
# restaurant_granu.receive_rate('Grazielle', 3)

# restaurant_coco_bambu.receive_rate('Gabriel', 5)
# restaurant_coco_bambu.receive_rate('Grazielle', 4)

# restaurant_il_piacere.receive_rate('Gabriel', 5)
# restaurant_il_piacere.receive_rate('Grazielle', 5)

juice_drink = Drink('Suco de laranja', 5, '500ml')
bread_dish = Dish('Pão de queijo', 4, 'Mini pão de queijo')

def main():
    print(bread_dish)
    print(juice_drink)
    # Restaurant.display_restaurants()

if __name__ == '__main__':
    main()