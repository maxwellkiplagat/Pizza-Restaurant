from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from server.controllers.restaurant_controller import restaurant_controller
    from server.controllers.pizza_controller import pizza_controller
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_controller

    app.register_blueprint(restaurant_controller)
    app.register_blueprint(pizza_controller)
    app.register_blueprint(restaurant_pizza_controller)

    return app

app = create_app()
