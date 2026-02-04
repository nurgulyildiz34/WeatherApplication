import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Weather App")
root.geometry("350x400")
root.config(bg="black")

# Neon Yeşil Renk Kodu: #39FF14
neon_green = "#39FF14"

city_label = tk.Label(root, text="CITY", bg="black", fg=neon_green, font=("Courier", 14, "bold"))
city_label.pack(pady=(30, 5))

# Entry (Giriş Kutusu)
city_entry = tk.Entry(root, bg="#121212", fg=neon_green, insertbackground=neon_green)
city_entry.pack(pady=5)

# Buton
fetch_button = tk.Button(root, text="FETCH WEATHER", bg="black", fg=neon_green,
                         activebackground=neon_green, activeforeground="black")
fetch_button.pack(pady=25)

# Sonuç Etiketi
weather_label = tk.Label(root, text="", bg="black", fg=neon_green, font=("Courier", 12))
weather_label.pack(pady=20)


def fetch_weather():
    city = city_entry.get()
    api_key = "00cd2eb2194b9512df956b87fc6e6e0d"
    # lang=tr ekleyerek hava durumunu Türkçe yapabilirsin
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_label.config(text=f"Sıcaklık: {temperature}°C\nDurum: {weather.upper()}")
        else:
            messagebox.showerror("Hata", "Şehir bulunamadı!")

    except Exception:
        messagebox.showerror("Hata", "Bağlantı sorunu oluştu")


fetch_button.config(command=fetch_weather)

root.mainloop()
