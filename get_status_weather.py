import tkinter as tk
import requests
import json

root = tk.Tk()

# Add a label
label = tk.Label(root, text="Enter a city name or zip code:")
label.pack()

# Add a text box
textbox = tk.Entry(root)
textbox.pack()

# Add a button
button = tk.Button(root, text="Get Weather")
button.pack()

def get_weather():
    location = textbox.get()
    api_key = "YOUR_API_KEY_HERE"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract relevant information from the response
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    # Update the GUI to display the weather data
    output = f"Temperature: {temp} K\nHumidity: {humidity}%\nWind speed: {wind_speed} m/s\nDescription: {description}"
    result_label = tk.Label(root, text=output)
    result_label.pack()

button.config(command=get_weather)

# Set the size of the window
root.geometry("300x200")

# Display the GUI window
root.mainloop()
