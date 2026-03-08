import os
import webbrowser
import threading
import requests
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Map weather icon prefix → CSS theme class
THEME_MAP = {
    "01": "theme-clear",
    "02": "theme-few-clouds",
    "03": "theme-cloudy",
    "04": "theme-cloudy",
    "09": "theme-rain",
    "10": "theme-rain",
    "11": "theme-storm",
    "13": "theme-snow",
    "50": "theme-mist",
}


def get_theme(icon_code: str) -> str:
    prefix = icon_code[:2] if icon_code else "01"
    return THEME_MAP.get(prefix, "theme-clear")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "").strip()
    if not city:
        return redirect(url_for("index"))

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=8)
    except requests.exceptions.ConnectionError:
        return render_template("error.html", city=city, reason="Sin conexión a internet.")
    except requests.exceptions.Timeout:
        return render_template("error.html", city=city, reason="La solicitud tardó demasiado.")

    if response.status_code == 404:
        return render_template("error.html", city=city, reason="Ciudad no encontrada.")
    elif response.status_code == 401:
        return render_template("error.html", city=city, reason="API Key inválida. Revisa tu archivo .env.")
    elif response.status_code != 200:
        return render_template("error.html", city=city, reason=f"Error del servidor ({response.status_code}).")

    data = response.json()

    # ── Extract & transform fields ──────────────────────────────────────────
    main      = data.get("main", {})
    wind      = data.get("wind", {})
    clouds    = data.get("clouds", {})
    sys_info  = data.get("sys", {})
    weather_d = data.get("weather", [{}])[0]

    visibility_m  = data.get("visibility", 0)           # metres
    wind_speed_ms = wind.get("speed", 0)                # m/s → km/h

    ctx = {
        "city":         data.get("name", city),
        "country_code": sys_info.get("country", "").lower(),
        "country_name": sys_info.get("country", ""),
        "description":  weather_d.get("description", "").capitalize(),
        "icon":         weather_d.get("icon", "01d"),
        "temp":         round(main.get("temp", 0), 1),
        "feels_like":   round(main.get("feels_like", 0), 1),
        "temp_min":     round(main.get("temp_min", 0), 1),
        "temp_max":     round(main.get("temp_max", 0), 1),
        "humidity":     main.get("humidity", 0),
        "pressure":     main.get("pressure", 0),
        "wind_speed":   round(wind_speed_ms * 3.6, 1),  # km/h
        "visibility":   round(visibility_m / 1000, 1),  # km
        "clouds":       clouds.get("all", 0),
        "theme":        get_theme(weather_d.get("icon", "01d")),
    }

    return render_template("weather.html", **ctx)


@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", city="", reason="Página no encontrada."), 404


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    # Open browser after a short delay so Flask is ready
    threading.Timer(1.2, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=False)
