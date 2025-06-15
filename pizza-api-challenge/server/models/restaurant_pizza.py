from server.app import db

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizza"
    __table_args__ = {'extend_existing': True}  
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)

    def validate(self):
        return 1 <= self.price <= 30
