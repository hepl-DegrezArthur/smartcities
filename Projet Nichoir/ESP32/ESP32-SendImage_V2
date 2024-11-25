import camera
import network
from umqtt.simple import MQTTClient
import time
import machine

# Configuration des broches
LED = machine.Pin(4, machine.Pin.OUT)

# Paramètres réseau Wi-Fi
ssid = 'A54 de arthur'
password = 'cacaprout'
#ssid = 'Proximus-Home-3890'       
#password = 'whn3ajbkbpjre' 

# Paramètres du serveur Mosquitto
mqtt_broker = "192.168.20.94"
mqtt_port = 1883
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
            time.sleep(1)  # Ajouter une pause pour éviter une boucle trop rapide
    print('Network connected:', sta_if.ifconfig())

# Publier un message sur un topic avec authentification
def publish_message(ToSend, topic):
    try:
        # Créer un client MQTT avec authentification
        client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
        
        # Se connecter au serveur MQTT
        client.connect()
        
        # Publier le message sur le topic
        if isinstance(ToSend, (int, float)):
            ToSend = str(ToSend)  # Convertir les nombres en chaîne
        client.publish(topic, ToSend)

        print(f"Message publié sur {topic}: {ToSend}")
        
        # Se déconnecter du serveur MQTT
        client.disconnect()
    except Exception as e:
        print("Erreur lors de la publication MQTT :", e)

# Connexion au Wi-Fi
connect_to_wifi()

# Attendre que le Wi-Fi soit connecté avant de publier
time.sleep(2)

try:
    # Envoyer le niveau de batterie
    BatLevel = 32
    publish_message(BatLevel, topic_Batterie)
    
    # Prendre une photo (avec la lumière)
    LED.value(1)
    camera.init()
    img = camera.capture()
    LED.value(0)
    camera.deinit()
    # Publier la photo
    publish_message(bytearray(img), topic_Photos)

    # Attendre 2 secondes
    time.sleep(2)
except Exception as e:
    time.sleep(0.5)

