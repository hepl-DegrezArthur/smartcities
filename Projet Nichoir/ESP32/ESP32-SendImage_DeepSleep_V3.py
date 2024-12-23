import machine
import time
import camera
import network
from umqtt.simple import MQTTClient

# Configuration des broches
LED = machine.Pin(12, machine.Pin.OUT)  # LED sur GPIO 12
pir = machine.Pin(15, machine.Pin.IN)   # PIR sur GPIO 15

# Configurer le réveil sur l'interruption externe (EXT0)
pir.irq(trigger=machine.Pin.IRQ_RISING, handler=lambda pin: machine.deepsleep())  # Wake up from deep sleep on PIR signal

# Temps maximum avant un réveil du Deep Sleep
SLEEP_DURATION_MS = 10 * 1000  # 10 secondes pour test

# Paramètres réseau Wi-Fi
ssid = 'WiFi-2.4-74AC'
password = 'wea42cus35ywe'

# Paramètres du serveur Mosquitto
mqtt_broker = "192.168.1.59"
mqtt_port = 1883
mqtt_user = 'RaspberryAD'
mqtt_pass = 'RaspberryAD'
topic_Photos = "ProjetNichoir_Photos"
topic_Batterie = "ProjetNichoir_Batterie"

# Se connecter au réseau Wi-Fi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, password)
        start_time = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start_time) > 5000:  # Timeout après 5 secondes
                break
        # Désactiver le Wi-Fi après l'utilisation
        if sta_if.isconnected():
            return True
        else:
            sta_if.active(False)
            return False
    return True

# Publier un message sur un topic avec authentification
def publish_message(ToSend, topic):
    try:
        client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
        client.connect()
        if isinstance(ToSend, (int, float)):
            ToSend = str(ToSend)
        client.publish(topic, ToSend)
        client.disconnect()
    except:
        pass  # Ignorer les erreurs pour économiser des ressources

def TakeAndSendPhotoAndBat():
    try:
        # Simuler le niveau de batterie
        BatLevel = 32

        # Envoyer le niveau de batterie
        publish_message(BatLevel, topic_Batterie)

        # Prendre une photo
        LED.value(1)
        camera.init()
        img = camera.capture()
        LED.value(0)
        camera.deinit()

        # Publier la photo
        if img:
            publish_message(bytearray(img), topic_Photos)
    except:
        pass  # Ignorer les erreurs pour minimiser les interruptions

# Programme principal
if connect_to_wifi():
    TakeAndSendPhotoAndBat()
    time.sleep(1)

# Mettre l'ESP32 en Deep Sleep
machine.deepsleep(SLEEP_DURATION_MS)
