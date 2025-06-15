from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant import Restaurant

restaurant_controller = Blueprint("restaurant_controller", __name__)

@restaurant_controller.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@restaurant_controller.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({
        "id": r.id,
        "name": r.name,
        "address": r.address,
        "pizzas": [
            {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            }
            for rp in r.restaurant_pizzas
        ]
    })

@restaurant_controller.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(r)
    db.session.commit()
    return "", 204
