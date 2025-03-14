
# 🌟 Smart Light Control via MQTT

Welcome to **Smart Light Control**—a sleek web-based application that lets you toggle a virtual light bulb using MQTT! This project combines a stylish web interface with a Python script simulating an IoT device (like an ESP8266), bringing the magic of real-time communication to your fingertips. Whether you're a student, hobbyist, or IoT enthusiast, this project is a fun way to explore MQTT in action! 🚀

---

## 🎯 Project Overview

This project fulfills an assignment to create a web app that controls a simulated light over MQTT. Here’s the gist:

- **Web Interface**: A modern webpage with ON/OFF buttons and a live status display.
- **IoT Simulation**: A Python script acting as a virtual ESP8266, listening for commands and printing the light’s status.
- **MQTT Magic**: Uses the `broker.emqx.io` public MQTT broker to connect the web and Python components.

---

## 📂 Project Structure

```
smart-light-control/
├── index.html          # 🌐 Web interface with buttons and status
├── light_simulation.py # 🐍 Python script simulating the IoT device
└── README.md           # 📝 You're reading it!
```

---

## ✨ Features

- **Interactive UI** 🖱️: Click "ON" or "OFF" buttons to control the light, with a glowing bulb animation.
- **Real-Time Status** 📢: See "Light is ON" or "Light is OFF" instantly on the webpage.
- **Console Feedback** 💻: The Python script prints `💡 Light is TURNED ON` or `💡 Light is TURNED OFF` in your terminal.
- **Lightweight & Simple** ⚡: No complex setup—just a browser and Python!

---

## 🛠️ How to Set It Up

Follow these steps to get the light switching in no time!

### Prerequisites
- **Python 3.x** 🐍: Installed on your machine.
- **paho-mqtt** 📦: Install it via pip:
  ```bash
  pip install paho-mqtt
  ```
- **Web Browser** 🌍: Any modern browser (Chrome, Firefox, etc.).
- **Internet Connection** 🌐: To connect to `broker.emqx.io`.

### Step-by-Step Guide

1. **Clone or Download** 📥
   - Grab this repository:
     ```bash
     git clone https://github.com/aine1100/smart-light-control.git
     cd SMART-LIGHT
     ```

2. **Run the IoT Simulator** 🖥️
   - Open a terminal and start the Python script:
     ```bash
     python light_simulation.py
     ```
   - You’ll see:
     ```
     Attempting connection to broker broker.emqx.io...
     Successfully connected to MQTT broker
     Subscribed to topic: /student_group/light_control
     ```

3. **Launch the Web Interface** 🌐
   - Open `index.html` in your browser (e.g., double-click the file or use a local server like `python -m http.server` and visit `localhost:8000`).
   - The page will load with a cool light bulb and buttons.

4. **Test It Out** 🕹️
   - Click "ON"—watch the bulb glow and check the terminal for `💡 Light is TURNED ON`.
   - Click "OFF"—see the bulb dim and `💡 Light is TURNED OFF` in the terminal.
   - The web status updates too: "Status: Light is ON/OFF".

5. **Shut Down** ⛔
   - Stop the Python script with `Ctrl+C` in the terminal:
     ```
     Shutting down MQTT client...
     ```

---

## 🚀 How It Works

### Web Interface (`index.html`)
- **Tech**: HTML, CSS, JavaScript + MQTT.js (WebSockets).
- **Broker**: Connects to `ws://broker.emqx.io:8083/mqtt`.
- **Topic**: Publishes "ON" or "OFF" to `/student_group/light_control`.
- **UI**: A glowing bulb, ON/OFF buttons, and a status bar with a modern light theme.

### IoT Simulator (`light_simulation.py`)
- **Tech**: Python with `paho-mqtt`.
- **Broker**: Connects to `broker.emqx.io:1883` (standard MQTT).
- **Topic**: Subscribes to `/student_group/light_control`.
- **Output**: Prints light status to the console.

### Communication Flow
```
[Web Browser] --> [MQTT Broker] --> [Python Script]
   "ON"/"OFF"       broker.emqx.io      💡 Status
```

---

## 🎨 Screenshots

### Web Interface
- **Light OFF**: Dim bulb, "Status: Light is OFF".
- **Light ON**: Glowing bulb, "Status: Light is ON".

### Console Output
```
💡 Light is TURNED ON
💡 Light is TURNED OFF
```

---

## ⚙️ Technical Details

- **MQTT Broker**: `broker.emqx.io` (public, free).
- **Ports**:
  - Web: 8083 (WebSockets).
  - Python: 1883 (standard MQTT).
- **Topic**: `/student_group/light_control`.
- **Dependencies**:
  - Web: MQTT.js (loaded via CDN).
  - Python: `paho-mqtt`.

---

## 🐛 Troubleshooting

- **No console output?**
  - Ensure the Python script is running before clicking buttons.
  - Verify internet connectivity to `broker.emqx.io`.
- **Buttons disabled?**
  - Wait for the web interface to connect (status turns green 🟢).
- **Errors?**
  - Check the browser console (F12) or Python terminal for logs.

---

## Why It’s Awesome

- **Educational**: Learn MQTT, WebSockets, and IoT basics.
- **Visual**: The glowing bulb and status updates make it fun!
- **Portable**: Runs locally with minimal setup.

---

## 📜 License

This project is open-source under the [MIT License](LICENSE). Feel free to use, modify, and share!

---

## 🙌 Acknowledgments

- **EMQX**: For the free MQTT broker.
- **MQTT.js**: For WebSocket support.
- **You**: For checking out this project!

---

⭐ **Star this repo if you liked it!** Questions? Open an issue or reach out. Let’s keep the lights on (or off) together! 💡

---

