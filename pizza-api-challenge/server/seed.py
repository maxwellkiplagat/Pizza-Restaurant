from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    r1 = Restaurant(name="Mario's Pizza", address="123 Main Street")
    r2 = Restaurant(name="Luigi's Slice", address="456 Elm Street")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Oak Avenue")

    db.session.add_all([r1, r2, r3])
    db.session.commit()

    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Onions, Peppers, Mushrooms")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Seed RestaurantPizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=9, restaurant_id=r2.id, pizza_id=p3.id)
    rp4 = RestaurantPizza(price=11, restaurant_id=r3.id, pizza_id=p1.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("✅ Database seeded!")
