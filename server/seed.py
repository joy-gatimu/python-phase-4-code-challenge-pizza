from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # This will delete any existing rows so you can run the seed file multiple times without duplicates
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    # Creating restaurants
    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')
    restaurants = [shack, bistro, palace]

    # Creating pizzas
    print("Creating pizzas...")
    cheese = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    pizzas = [cheese, pepperoni, california]

    # Creating RestaurantPizza entries
    print("Creating RestaurantPizza...")
    pr1 = RestaurantPizza(restaurant=shack, pizza=cheese, price=1)
    pr2 = RestaurantPizza(restaurant=bistro, pizza=pepperoni, price=4)
    pr3 = RestaurantPizza(restaurant=palace, pizza=california, price=5)
    restaurantPizzas = [pr1, pr2, pr3]

    # Check if price is being passed correctly
    print(f"RestaurantPizza entries: {restaurantPizzas}")

    # Add all to the session and commit
    try:
        db.session.add_all(restaurants)
        db.session.add_all(pizzas)
        db.session.add_all(restaurantPizzas)
        db.session.commit()
        print("Seeding done!")
    except Exception as e:
        db.session.rollback()
        print(f"Error during commit: {e}")
