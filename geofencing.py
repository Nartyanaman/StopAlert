import tkinter as tk
import requests
from geopy.distance import geodesic

# Define geofence center and radius
geofence_center = (43.7064, -79.3986)  # Example: Brampton Gateway Terminal (can be any location)
geofence_radius = 0.5  # Radius in kilometers

# Function to get the current location of the device via IP Geolocation
def get_ip_location():
    # Use a free IP geolocation API (you can also use paid services for more accuracy)
    api_url = 'http://ipinfo.io/json'  # Fetches IP address and approximate location
    response = requests.get(api_url)
    data = response.json()
    
    # Extract latitude and longitude from the response (if available)
    location = data.get("loc", "").split(",")
    if len(location) == 2:
        latitude = location[0]
        longitude = location[1]
        return latitude, longitude
    else:
        return None, None

# Function to check if the user is within the geofence
def is_within_geofence(user_location, geofence_center, radius):
    distance = geodesic(user_location, geofence_center).kilometers
    return distance <= radius

# Function to update the location and geofence status in the GUI
def update_location():
    user_location = get_ip_location()
    
    if user_location[0] and user_location[1]:
        location_label.config(text=f"Current Location: {user_location}")
        
        # Check if within geofence
        if is_within_geofence(user_location, geofence_center, geofence_radius):
            status_label.config(text="Status: Within Geofence", fg="green")
            request_button.config(state=tk.NORMAL)  # Enable the button
        else:
            status_label.config(text="Status: Outside Geofence", fg="red")
            request_button.config(state=tk.DISABLED)  # Disable the button
    else:
        location_label.config(text="Failed to retrieve location.")
    
    root.after(5000, update_location)  # Update every 5 seconds

# Function to handle the request button action
def send_request():
    status_label.config(text="Request sent successfully!", fg="blue")

# Initialize Tkinter root window
root = tk.Tk()
root.title("Geofencing App")
root.geometry("400x300")

# Create and place widgets
title_label = tk.Label(root, text="Geofencing Feature Activated", font=("Helvetica", 16))
title_label.pack(pady=10)

geofence_info = tk.Label(root, text=f"Geofence Center: {geofence_center}\nRadius: {geofence_radius} km", font=("Helvetica", 10))
geofence_info.pack(pady=10)

location_label = tk.Label(root, text="Current Location: Fetching...", font=("Helvetica", 12))
location_label.pack(pady=10)

status_label = tk.Label(root, text="Status: Checking geofence...", font=("Helvetica", 12))
status_label.pack(pady=10)

request_button = tk.Button(root, text="Send Request", font=("Helvetica", 12), state=tk.DISABLED, command=send_request)
request_button.pack(pady=20)

# Start updating the location
update_location()

# Run the Tkinter event loop
root.mainloop()