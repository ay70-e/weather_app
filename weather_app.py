#Create by Aya Laheb
# Date 5/12/2024


# This is a Python-based Weather App created using the Tkinter library for GUI development. 
# The app allows users to search for the current weather conditions of a city by entering the city's name.
# It retrieves weather information such as temperature, humidity, wind speed, and atmospheric pressure 
# from the OpenWeatherMap API using the city's latitude and longitude obtained through the GeoPy library.
# The GUI includes an interactive search bar, buttons, labels for displaying weather data, and a live clock
# displaying the current time in the searched location.

# The following libraries and tools are used:
# - Tkinter: For building the graphical user interface.
# - GeoPy: For geocoding the city name to latitude and longitude.
# - timezonefinder and pytz: For finding and displaying the local timezone and current time.
# - requests: For making API calls to OpenWeatherMap to fetch weather data.
# - OpenWeatherMap API: The external API used to provide weather details.


from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfied.get()
    geolocator = Nominatim(user_agent="my_weather_app@example.com")  # Update user agent
    location = geolocator.geocode(city)

    if location is None:
        messagebox.showerror("Error", "City not found")
        return

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    # Fetch weather data using latitude and longitude
    api_key = "97e2a25df168bc2c5db155e788e0d350"  # Replace with your OpenWeatherMap API key
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}&units=metric"
    
    try:
        json_data = requests.get(api).json()
        if json_data['cod'] != 200:
            messagebox.showerror("Error", json_data.get("message", "Error fetching weather data"))
            return
        
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'])
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°C"))
        w.config(text=(wind, "m/s"))
        h.config(text=(humidity, "%"))
        d.config(text=description)
        p.config(text=json_data['main']['pressure'])

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Search box
search_image = PhotoImage(file='search.png')
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfied = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfied.place(x=50, y=40)
textfied.focus()

search_icon = PhotoImage(file='search_icon.png')
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file='logo3.png')
logo = Label(image=logo_image)
logo.place(x=145, y=100)

# Button box
Frame_image = PhotoImage(file="box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
Label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label1.place(x=120, y=400)

Label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label2.place(x=250, y=400)

Label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label3.place(x=430, y=400)

Label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
Label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=("arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=670, y=430)

# Start the Tkinter main loop
root.mainloop()