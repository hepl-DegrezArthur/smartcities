import os
import paho.mqtt.client as mqtt
from PIL import Image
import io
import time

# Paramètres du broker MQTT
mqtt_broker = "192.168.1.26"  # Remplacez par l'adresse IP de votre broker
mqtt_port = 1883                # Port par défaut pour MQTT
mqtt_topic_Photos = "ProjetNichoir_Photos"     # Nom du topic pour recevoir l'image

# Identifiants pour la connexion
mqtt_user = "RaspberryAD"        # Remplacez par votre nom d'utilisateur
mqtt_pass = "RaspberryAD"        # Remplacez par votre mot de passe

# Répertoire pour stocker les photos
photo_directory = "/var/www/html/nichoir"  # Remplacez par votre chemin
max_photos = 50  # Nombre maximum de photos autorisées dans le répertoire

# Liste pour stocker les données de l'image
image_data = bytearray()

# Fonction pour trouver le numéro de la prochaine image
def get_next_image_number():
    # Liste les fichiers dans le répertoire
    existing_files = [f for f in os.listdir(photo_directory) if f.startswith("image") and f.endswith(".jpg")]
    # Trier les fichiers par numéro
    existing_files.sort(key=lambda x: int(x.replace("image", "").replace(".jpg", "")))
    if existing_files:
        last_file = existing_files[-1]
        last_number = int(last_file.replace("image", "").replace(".jpg", ""))
        return last_number + 1
    return 0

# Fonction pour limiter le nombre de photos dans le dossier
def manage_photo_limit():
    # Liste les fichiers dans le répertoire
    existing_files = [f for f in os.listdir(photo_directory) if f.startswith("image") and f.endswith(".jpg")]
    # Trier les fichiers par numéro croissant
    existing_files.sort(key=lambda x: int(x.replace("image", "").replace(".jpg", "")))
    # Supprimer les fichiers si le nombre dépasse la limite
    while len(existing_files) > max_photos:
        oldest_file = os.path.join(photo_directory, existing_files.pop(0))
        os.remove(oldest_file)
        print(f"Photo supprimée : {oldest_file}")

# Fonction appelée lorsqu'un message est reçu
def on_message(client, userdata, msg):
    global image_data

    # Ajouter les données du message reçu à l'image
    image_data.extend(msg.payload)
    print(f"Morceau reçu, taille totale actuelle : {len(image_data)} octets")

# Fonction pour traiter et stocker l'image
def process_and_store_image():
    global image_data

    try:
        # Convertir les données en image en utilisant un flux mémoire (BytesIO)
        image_stream = io.BytesIO(image_data)
        image = Image.open(image_stream)

        # Vérifier et créer le répertoire si nécessaire
        if not os.path.exists(photo_directory):
            os.makedirs(photo_directory)

        # Obtenir le numéro de la prochaine image
        next_image_number = get_next_image_number()
        image_path = os.path.join(photo_directory, f"image{next_image_number}.jpg")

        # Sauvegarder l'image
        image.save(image_path)
        print(f"Image sauvegardée : {image_path}")

        # Gérer la limite des photos
        manage_photo_limit()

    except Exception as e:
        print("Erreur lors de l'interprétation de l'image :", e)

    # Réinitialiser les données après traitement
    image_data.clear()

# Fonction appelée lors de la connexion au broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT avec succès")
        client.subscribe(mqtt_topic_Photos)  # S'abonner au topic après la connexion
        print(f"Abonné au topic '{mqtt_topic_Photos}'")
    else:
        print("Échec de la connexion, code de retour:", rc)

# Configuration du client MQTT
client = mqtt.Client("image_receiver")
client.username_pw_set(mqtt_user, mqtt_pass)  # Configuration des identifiants
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker MQTT
print("Connexion au broker MQTT...")
client.connect(mqtt_broker, mqtt_port)

# Boucle d'attente des messages avec traitement périodique de l'image
try:
    client.loop_start()
    while True:
        # Traiter et afficher l'image toutes les secondes si des données sont disponibles
        time.sleep(1)
        if image_data:
            process_and_store_image()
except KeyboardInterrupt:
    print("Déconnexion du client MQTT")
    client.loop_stop()
    client.disconnect()
