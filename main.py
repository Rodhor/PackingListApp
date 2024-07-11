from flask import request, jsonify
from config import db, app
from models import Items


@app.route("/items", methods=["GET"])
def get_items():
    items = Items.query.all()
    json_items = list(map(lambda x: x.to_json(), items))
    return jsonify({"items": json_items})


@app.route("/create_item", methods=["POST"])
def create_item():
    data = request.json
    name = data.get("name")
    category = data.get("category")
    days_of_usage = data.get("days_of_usage")
    weather_usage = data.get("weather_usage")
    weight = data.get("weight")
    volume = data.get("volume")
    is_essential = data.get("is_essential")
    is_fragile = data.get("is_fragile")
    notes = data.get("notes")

    if not name:
        return jsonify({"message": "You must provide an item name!"}), 400

    new_item = Items(
        name=name,
        category=category,
        days_of_usage=days_of_usage,
        weather_usage=weather_usage,
        weight=weight,
        volume=volume,
        is_essential=is_essential,
        is_fragile=is_fragile,
        notes=notes,
    )

    try:
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item created!", "item": new_item.to_json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Failed to create item: {str(e)}"}), 400


if __name__ == "__main__":
    with app.app_context():
        db.create_all(bind_key=None)  # Creates tables for the default database
        db.create_all(bind_key="trips")  # Creates tables for the trips database

    app.run(debug=True)
