# StopAlert

**StopAlert** is a smart bus stop notification system that enables users to request bus stops based on their real-time location. It uses Flask, SocketIO, and geofencing to send notifications to bus drivers when users are within a predefined range of bus stops. This ensures efficient and dynamic transportation services by leveraging location-based alerts.

---

## Features

- **Real-time Notifications**: Sends bus stop requests to drivers via WebSocket (SocketIO).
- **Geofencing**: Uses geofencing to check if a user is within the required proximity of a bus stop before allowing a request.
- **Location-Based Requests**: Users can request bus stops based on their GPS location, and the system checks their proximity to predefined bus stops.
- **Simple UI**: The system includes a basic Tkinter GUI for user interaction and bus stop management.

---

## Technologies Used

- **Flask**: A lightweight web framework for Python to build the API.
- **SocketIO**: Real-time communication between users and the server.
- **Geopy**: Used for calculating distances between user location and bus stops.
- **Tkinter**: Python's built-in library for creating simple GUIs.
- **Requests**: For sending API requests and handling responses.
- **Flask-SocketIO**: For handling WebSocket connections.

---

