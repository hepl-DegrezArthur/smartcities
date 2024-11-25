import camera
import network
from umqtt.simple import MQTTClient
import time
import machine

# Configuration des broches
LED = machine.Pin(4, machine.Pin.OUT)  # LED sur GPIO 4
pir = machine.Pin(15, machine.Pin.IN)  # PIR sur GPIO 15

# Paramètres réseau Wi-Fi
ssid = 'A54 de arthur'  # Remplacez par votre SSID Wi-Fi
password = 'cacaprout'  # Remplacez par votre mot de passe Wi-Fi

# Paramètres du serveur Mosquitto
mqtt_broker = "192.168.20.94"  # Remplacez par l'adresse IP de votre broker
mqtt_port = 1883  # Port MQTT par défaut
mqtt_user = 'RaspberryAD'  # Nom d'utilisateur MQTT
mqtt_pass = 'RaspberryAD'   # Mot de passe MQTT
topic_Photos = "ProjetNichoir_Photos"
topic_Batterie = "ProjetNichoir_Batterie"

# Se connecter au réseau Wi-Fi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        #print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    #print('Network connected:', sta_if.ifconfig())

# Publier un message sur un topic avec authentification
def publish_message(ToSend, topic):
    # Créer un client MQTT avec authentification
    client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
    
    # Se connecter au serveur MQTT
    client.connect()
    
    # Publier le message sur le topic
    client.publish(topic, ToSend)

    #print("Message publié :", topic)
    
    # Se déconnecter du serveur MQTT
    client.disconnect()

# Connexion au Wi-Fi
connect_to_wifi()

# Attendre que le Wi-Fi soit connecté avant de publier
time.sleep(2)

try:
    while True:
        if pir.value() == 1:  # Détection de mouvement
            #print("Mouvement détecté !")
            
            # Prendre une photo
            LED.value(1)
            camera.init()
            img = camera.capture()
            LED.value(0)
            camera.deinit()
            
            # Publier la photo
            publish_message(img, topic_Photos)
            time.sleep(2)
            # Attendre que le mouvement cesse
            while pir.value() == 1:
                time.sleep(0.1)
            #print("Plus de mouvement.")
except KeyboardInterrupt:
    time.sleep(0.1)
