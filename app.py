from models.restaurant import Restaurant

restaurant_granu = Restaurant('Granulado', 'Doceria')
restaurant_coco_bambu = Restaurant('Coco Bambu', 'Frutos do mar')
restaurant_il_piacere = Restaurant('Il Piacere', 'Pizzaria')

Restaurant.change_state(restaurant_granu)

restaurant_granu.receive_rate('Gabriel', 3)
restaurant_granu.receive_rate('Grazielle', 3)

restaurant_coco_bambu.receive_rate('Gabriel', 5)
restaurant_coco_bambu.receive_rate('Grazielle', 4)

restaurant_il_piacere.receive_rate('Gabriel', 5)
restaurant_il_piacere.receive_rate('Grazielle', 5)

def main():
    Restaurant.display_restaurants()

if __name__ == '__main__':
    main()