import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io

API_KEY = "741f3b9e1b58415d918173624253001"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

root = tk.Tk()
root.title("Weather App")
root.geometry("500x600")  
root.config(bg="#f0f4f7")  

header_frame = tk.Frame(root, bg="#42a5f5", bd=5)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Weather App", font=("Helvetica", 18, "bold"), bg="#42a5f5", fg="white")
header_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City:", font=("Arial", 14), bg="#f0f4f7")
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=30, relief="solid")
city_entry.pack(pady=5)

get_weather_button = ttk.Button(root, text="Get Weather", command=lambda: get_weather(), style="W.TButton")
get_weather_button.pack(pady=20)

weather_frame = tk.Frame(root, bg="#f0f4f7")
weather_frame.pack(pady=10)

city_display = tk.Label(weather_frame, text="", font=("Arial", 16, "bold"), bg="#f0f4f7")
city_display.grid(row=0, column=0, padx=10, pady=5)

temp_label = tk.Label(weather_frame, text="", font=("Arial", 14), bg="#f0f4f7")
temp_label.grid(row=1, column=0, padx=10, pady=5)

condition_label = tk.Label(weather_frame, text="", font=("Arial", 14), bg="#f0f4f7")
condition_label.grid(row=2, column=0, padx=10, pady=5)

humidity_label = tk.Label(weather_frame, text="", font=("Arial", 12), bg="#f0f4f7")
humidity_label.grid(row=3, column=0, padx=10, pady=5)

wind_label = tk.Label(weather_frame, text="", font=("Arial", 12), bg="#f0f4f7")
wind_label.grid(row=4, column=0, padx=10, pady=5)

icon_label = tk.Label(weather_frame, bg="#f0f4f7")
icon_label.grid(row=0, column=1, rowspan=5, padx=10)

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        update_weather_display(data)
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error. Please check your internet connection.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def update_weather_display(data):
    city_name = data['location']['name']
    country_name = data['location']['country']
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_kph']
    icon_url = "http:" + data["current"]["condition"]["icon"]

    city_display.config(text=f"{city_name}, {country_name}")
    temp_label.config(text=f"Temperature: {temperature}°C")
    condition_label.config(text=f"Condition: {condition}")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_label.config(text=f"Wind Speed: {wind_speed} km/h")

    icon_response = requests.get(icon_url)
    img_data = Image.open(io.BytesIO(icon_response.content))
    img_data = img_data.resize((100, 100), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(img_data)

    icon_label.config(image=icon)
    icon_label.image = icon  

style = ttk.Style()
style.configure("W.TButton", font=("Helvetica", 14), background="#42a5f5", foreground="black", padding=10)
style.map("W.TButton", background=[('active', '#1e88e5')])

root.mainloop()
