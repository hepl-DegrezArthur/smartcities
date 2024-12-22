import machine
import camera
import network
from umqtt.simple import MQTTClient

# Configuration des broches
LED = machine.Pin(12, machine.Pin.OUT)  # LED sur GPIO 12
pir = machine.Pin(15, machine.Pin.IN)  # PIR sur GPIO 15

# ADC Configuration
adc = machine.ADC(machine.Pin(13))
adc.width(machine.ADC.WIDTH_12BIT)
adc.atten(machine.ADC.ATTN_6DB)  # Réduction pour économiser l'énergie

# Wi-Fi Parameters
ssid = 'WiFi-2.4-74AC'
password = 'wea42cus35ywe'

# MQTT Configuration
mqtt_broker = "192.168.1.59"
mqtt_port = 1883
mqtt_user = 'RaspberryAD'
mqtt_pass = 'RaspberryAD'
topic_Photos = "ProjetNichoir_Photos"
topic_Batterie = "ProjetNichoir_Batterie"

# Deep Sleep Duration (10s)
SLEEP_DURATION_MS = 10 * 1000

# Connect to Wi-Fi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass

# Publish a message with MQTT
def publish_message(ToSend, topic):
    try:
        client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
        client.connect()
        client.publish(topic, str(ToSend) if isinstance(ToSend, (int, float)) else ToSend)
        client.disconnect()
    except Exception:
        pass

# Take photo and send battery level
def take_and_send_photo_and_bat():
    try:
        publish_message(32, topic_Batterie)  # Mock battery level
        LED.value(1)
        camera.init()
        img = camera.capture()
        LED.value(0)
        camera.deinit()
        publish_message(bytearray(img), topic_Photos)
    except Exception:
        pass

# Main Program
if __name__ == "__main__":
    connect_to_wifi()
    take_and_send_photo_and_bat()
    machine.deepsleep(SLEEP_DURATION_MS)

