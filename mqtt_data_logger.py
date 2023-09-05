import paho.mqtt.client as mqtt
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'user',
    'password': 'password',
    'database': 'mqtt_data'
}

# MQTT configuration
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected with Code: " + str(rc))
    client.subscribe("test/#")  # Replace with your topic name

def on_message(client, userdata, msg):
    print("Message received: " + msg.payload.decode("utf-8"))
    store_in_db(msg.topic, msg.payload.decode("utf-8"))

def store_in_db(topic, payload):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    query = "INSERT INTO mqtt_messages (topic, payload) VALUES (%s, %s)"
    cursor.execute(query, (topic, payload))
    connection.commit()

    cursor.close()
    connection.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
