import requests
import tkinter as tk

# Bus stop simulation (input user location manually here)
user_location = (40.7129, -74.0061)  # Example user location near Stop_1

def request_stop(route):
    response = requests.post("http://localhost:5000/request_stop", json={
        "route": route,
        "location": user_location
    })
    if response.ok:
        status_label.config(text=response.json()["message"])
    else:
        status_label.config(text=response.json()["error"])

# Basic GUI using Tkinter
app = tk.Tk()
app.title("Bus Stop")

# Label and buttons
label = tk.Label(app, text="Select bus route to request stop:")
label.pack()

for route in ["501", "7", "201"]:
    btn = tk.Button(app, text=f"Request Stop for Route {route}", command=lambda r=route: request_stop(r))
    btn.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
