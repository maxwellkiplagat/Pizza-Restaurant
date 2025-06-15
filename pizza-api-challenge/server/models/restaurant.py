from server.app import db
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = "restaurant"
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant", cascade="all, delete")
