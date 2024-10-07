# LCD - DHT11

## Explications du code 
Le script commence par importer les bibliothèques nécessaires, notamment pour gérer un écran LCD, effectuer des temporisations, interagir avec le matériel comme les broches GPIO et le PWM pour le buzzer, et lire les données d'un capteur DHT11 qui mesure la température et l'humidité.

Ensuite, une entrée analogique est définie pour un potentiomètre, et un buzzer est initialisé sur la broche GPIO 18. Des variables sont créées pour gérer le délai entre les notes et définir le volume initial. Le capteur DHT11 est initialisé pour lire les valeurs de température et d'humidité.

Le code configure également l'interface I2C pour communiquer avec l'écran LCD, spécifiant les broches de données et d'horloge. L'écran est ensuite initialisé pour afficher des informations.

Des fonctions sont définies pour chaque note musicale (DO, RE, MI, FA, SOL, LA, SI), permettant de jouer ces notes en réglant la fréquence et le volume du buzzer, puis en jouant la note pendant une durée spécifiée. Une fonction Nope() est incluse pour couper le son. (code repris du labo PWM)

La fonction BirthdaySong() permet de jouer la mélodie de "Joyeux Anniversaire", en appelant les fonctions de note avec des délais appropriés pour créer la séquence musicale.

Dans la boucle principale, le script lit régulièrement la température et l'humidité du capteur DHT11, affiche ces valeurs sur l'écran LCD, puis, si la température dépasse 30 degrés ou l'humidité dépasse 45 %, la chanson "Joyeux Anniversaire" est jouée.

## ChartFlow Diagramme
![image](https://github.com/user-attachments/assets/976c8fdd-bdd2-46a3-b240-6a7b0f910bac)
