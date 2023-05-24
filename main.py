def r1():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Название ресторана,  кухня ")

        def open_restaurant(self):
            print("Ресторан открыт")

    restaurant = Restaurant('Moris', 'французска')

    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
def r2():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
          self.restaurant_name = restaurant_name
          self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Название ресторана,  кухня")

        def open_restaurant(self):
            print("Ресторан открыт")

    restaurant1 = Restaurant('Moris', 'французская')
    restaurant2 = Restaurant('KFC', 'fast food')
    restaurant3 = Restaurant('Tor', 'немецкая')

    print(restaurant1.restaurant_name)
    print(restaurant1.cuisine_type)
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    print(restaurant2.restaurant_name)
    print(restaurant2.cuisine_type)
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    print(restaurant3.restaurant_name)
    print(restaurant3.cuisine_type)
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()

def r3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, reiting):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting = reiting

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто!')

        def write_reiting(self):
            print(fr'Бывший рейтинг: {self.reiting}')
            self.reiting = input('Обновлённое значение: ')
            print(fr'Обновлено: {self.reiting}')

    newRestaurant = Restaurant('Moris', 'французска', '5')
    newRestaurant.write_reiting()
r3()