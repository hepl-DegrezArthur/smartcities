import camera
import network
from umqtt.simple import MQTTClient
import time
import machine

LED = machine.Pin(4,machine.Pin.OUT)

# Paramètres réseau Wi-Fi
ssid = 'Proximus-Home-3890'       
password = 'whn3ajbkbpjre' 

# Paramètres du serveur Mosquitto
mqtt_broker = "192.168.1.26" 
mqtt_port = 1883  # Le port par défaut pour MQTT est 1883
mqtt_user = 'RaspberryAD' 
mqtt_pass = 'RaspberryAD'  
topic_Photos = "ProjetNichoir_Photos"
topic_Batterie = "ProjetNichoir_Batterie"

# Se connecter au réseau Wi-Fi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Network connected:', sta_if.ifconfig())

# Publier un message sur un topic avec authentification
def publish_message(ToSend, topic):
    # Créer un client MQTT avec authentification
    client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
    
    # Se connecter au serveur MQTT
    client.connect()
    
    # Publier le message sur le topic
    client.publish(topic, ToSend)

    print(ToSend)
    
    # Se déconnecter du serveur MQTT
    client.disconnect()

# Connexion au Wi-Fi
connect_to_wifi()

# Attendre que le Wi-Fi soit connecté avant de publier
time.sleep(2)

#Prendre une photo (avec la lumière)
LED.value(1)
camera.init()
img = camera.capture()
LED.value(0)
b=bytearray(img)
camera.deinit()

#Publier la photo
publish_message(b, topic_Photos)

#Attendre 2sec
time.sleep(2)
