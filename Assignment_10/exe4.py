from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/airport/<icao_code>')
def get_airport(icao_code):
    try:
        with open("Assignment_10/airports.json", "r", encoding="utf-8") as file:
            airports_data = json.load(file)
    except FileNotFoundError:
        return jsonify({"error": "Database file not found"}), 500

    for airport in airports_data.values():
        if airport.get("icao") == icao_code.upper():
            return jsonify({
                "icao": airport.get("icao"),
                "name": airport.get("name"),
                "city": airport.get("city"),
                "country": airport.get("country")
            })
            
    return jsonify({"error": "Airport not found"}), 404

app.run(port=5000)