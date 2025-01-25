from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import geopy.distance

app = Flask(__name__)
socketio = SocketIO(app)

# Predefined bus stop locations (latitude, longitude)
bus_stops = {
    "Stop_1": (40.7128, -74.0060),  # Example coordinates
    "Stop_2": (40.7138, -74.0070),
    "Stop_3": (40.7148, -74.0080),
}

# Check if a user is within a set range from a stop (in meters)
def is_near_stop(user_location, stop_location, range_meters=50):
    return geopy.distance.distance(user_location, stop_location).meters < range_meters

# Endpoint to request a stop for a specific bus route
@app.route('/request_stop', methods=['POST'])
def request_stop():
    data = request.json
    route = data.get('route')
    user_location = data.get('location')

    # Check if user is near any of the bus stops
    for stop_name, stop_location in bus_stops.items():
        if is_near_stop(user_location, stop_location):
            # Send request to bus drivers via SocketIO
            socketio.emit('stop_request', {'route': route, 'stop': stop_name})
            return jsonify({"message": f"Stop requested at {stop_name} for route {route}."}), 200

    return jsonify({"error": "Not near a bus stop"}), 400

# Start Flask-SocketIO server
if __name__ == '__main__':
    socketio.run(app, debug=True)