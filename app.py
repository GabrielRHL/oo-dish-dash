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

hot_chocolate_drink = Drink('Chocolate quente', 15, '300ml')
cheese_bread_dish = Dish('Pão de queijo', 10, 'Pão de queijo grande')

restaurant_granu.add_to_menu(cheese_bread_dish)
restaurant_granu.add_to_menu(hot_chocolate_drink)

def main():
    print(cheese_bread_dish)
    print(hot_chocolate_drink)
    # Restaurant.display_restaurants()

if __name__ == '__main__':
    main()