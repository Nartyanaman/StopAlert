import socketio
import tkinter as tk

# Initialize SocketIO client
sio = socketio.Client()

# Function to handle incoming stop requests
def handle_stop_request(data):
    route = data['route']
    stop = data['stop']
    status_label.config(text=f"Stop requested at {stop} for route {route}")

# Connect to the servers
sio.connect('http://localhost:5000')

# Bind the event listener for 'stop_request' to the function
sio.on('stop_request', handle_stop_request)

# Bus GUI using Tkinter
app = tk.Tk()
app.title("Bus")

status_label = tk.Label(app, text="Waiting for stop requests...")
status_label.pack()

app.mainloop()