import paho.mqtt.client as mqtt
import time

# MQTT broker details
BROKER_ADDRESS = "broker.emqx.io"
PORT_NUMBER = 1883
CONTROL_TOPIC = "/student_group/light_control"

# Callback triggered upon connecting to the MQTT broker
def handle_connection(client, userdata, flags, rc):
    print("Successfully connected to MQTT broker")
    client.subscribe(CONTROL_TOPIC)
    print(f"Subscribed to topic: {CONTROL_TOPIC}")

# Callback triggered when a message is received
def handle_message(client, userdata, msg):
    command = msg.payload.decode()
    if command == "ON":
        print("💡 Light is TURNED ON")
    elif command == "OFF":
        print("💡 Light is TURNED OFF")

def start_mqtt_client():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = handle_connection
    mqtt_client.on_message = handle_message
    print(f"Attempting connection to broker {BROKER_ADDRESS}...")
    mqtt_client.connect(BROKER_ADDRESS, PORT_NUMBER, 60)
    mqtt_client.loop_forever()

if __name__ == "__main__":
    try:
        start_mqtt_client()
    except KeyboardInterrupt:
        print("\nShutting down MQTT client...")