# 🌤️ ClimaP1 — Consulta el Clima Mundial

Aplicación web desarrollada con **Flask** que consulta el clima actual de cualquier ciudad del mundo usando la API de [OpenWeatherMap](https://openweathermap.org/). Presenta los datos de forma visual y atractiva, adaptando el diseño al tipo de clima detectado.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Características

| Dato | Descripción |
|------|-------------|
| 🌡️ Temperatura actual | En grados Celsius |
| 🤔 Sensación térmica | Temperatura percibida |
| 🔽🔼 Mín / Máx del día | Rango de temperatura |
| 💧 Humedad | Porcentaje relativo |
| 💨 Viento | Velocidad en km/h |
| 🔵 Presión | Presión atmosférica en hPa |
| 👁️ Visibilidad | En kilómetros |
| ☁️ Nubosidad | Porcentaje de cobertura |
| 🌐 Bandera del país | Via flagcdn.com |
| 🖼️ Ícono oficial | De OpenWeatherMap |

- 🎨 **Tema dinámico** — el fondo y colores cambian según el clima (Naranja para despejado, Azul para lluvia, Gris para nublado, Azul claro para nieve)
- ⚡ **Búsqueda optimizada** — sistema de caché en memoria para resultados instantáneos en búsquedas repetidas
- ❌ **Página de error amigable** — cuando la ciudad no existe, con botón para volver
- 🚀 **Auto-abre el navegador** al ejecutar el servidor

---

## 🗂️ Estructura del proyecto

```
ClimaP1/
├── app.py                  # Servidor Flask principal
├── .env                    # Variables de entorno (API Key) ← NO subir al repo
├── .env.example            # Plantilla pública de .env
├── requirements.txt        # Dependencias Python
├── .gitignore
├── templates/
│   ├── base.html           # Plantilla base (layout)
│   ├── index.html          # Formulario de búsqueda
│   ├── weather.html        # Resultados del clima
│   └── error.html          # Página de error amigable
└── static/
    ├── css/
    │   └── style.css       # Estilos + temas dinámicos
    └── js/
        └── main.js         # Interactividad UX
```

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/yovannycubas/AppClima.git
cd AppClima
```

### 2. Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

### 3. Obtener la API Key

1. Regístrate gratis en [openweathermap.org/api](https://openweathermap.org/api)
2. Activa el plan **Current Weather Data** (gratuito)
3. Copia tu API Key

### 4. Configurar la API Key

#### Opción A — Archivo `.env` (recomendada)

Crea un archivo `.env` en la raíz del proyecto (copia `.env.example`):

```
OPENWEATHER_API_KEY=aquí_tu_api_key
```

Luego ejecuta normalmente:

```bash
python app.py
```

#### Opción B — Variable de entorno en PowerShell (Windows)

```powershell
$env:OPENWEATHER_API_KEY="aquí_tu_api_key"; python app.py
```

#### Opción C — Variable de entorno en CMD (Windows)

```cmd
set OPENWEATHER_API_KEY=aquí_tu_api_key && python app.py
```

#### Opción D — Linux / macOS

```bash
OPENWEATHER_API_KEY="aquí_tu_api_key" python app.py
```

### 5. Abrir en el navegador

El servidor inicia en **http://127.0.0.1:5000** y **abre el navegador automáticamente**.

---

## 🌦️ Temas visuales adaptativos

El diseño cambia automáticamente según el clima de la ciudad buscada:

| Clima | Tema | Colores |
|-------|------|---------|
| ☀️ Despejado | `theme-clear` | Naranja (#ff8c00) |
| 🌤️ Pocas nubes | `theme-few-clouds` | Azul cielo |
| ☁️ Nublado | `theme-cloudy` | Gris (#7f8c8d) |
| 🌧️ Lluvia | `theme-rain` | Azul (#2980b9) |
| ⛈️ Tormenta | `theme-storm` | Azul noche / rojo |
| ❄️ Nieve | `theme-snow` | Azul claro / Cian |
| 🌫️ Niebla | `theme-mist` | Gris suave |

---

## 🛠️ Stack tecnológico

- **Backend**: Python 3.8+ · Flask · Requests · Python-dotenv
- **Frontend**: HTML5 · CSS3 (Glassmorphism, variables CSS, animaciones) · JavaScript vanilla
- **API**: OpenWeatherMap Current Weather Data
- **Fuentes**: Google Fonts — Inter
- **Banderas**: flagcdn.com

---

## 📡 Endpoints

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Formulario de búsqueda |
| `/weather?city=<ciudad>` | GET | Resultados del clima |
| Cualquier ruta inválida | — | Página de error 404 |

---

## ⚠️ Notas importantes

> [!IMPORTANT]
> El archivo `.env` **nunca debe subirse al repositorio**. Ya está en `.gitignore`.

> [!NOTE]
> Las API Keys gratuitas de OpenWeatherMap pueden tardar hasta **2 horas** en activarse después del registro.

---

## 📄 Licencia

MIT © 2026 – [yovannycubas](https://github.com/yovannycubas)
