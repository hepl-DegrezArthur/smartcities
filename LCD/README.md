J'ai personnelement utilisé l'interruption d'un timer afin de créé les délai de la LED. Afin de changer ce délai je redéfini mon interruption avec une valeur de compteur différente 
  ==> Il peut être interressant d'utiliser la fonction présentée par le prof : time.ticks_ms() et time.ticks_diff()


Le script commence par importer les bibliothèques nécessaires pour contrôler un écran LCD, gérer les temporisations, interagir avec le matériel (comme les broches GPIO et les périphériques ADC), et lire des données d'un capteur DHT11 (qui mesure la température et l'humidité).

Ensuite, il définit une entrée analogique pour un potentiomètre, initialise un buzzer sur la broche GPIO 18, et fixe quelques variables pour le délai entre les notes et le volume initial. Le capteur DHT est également initialisé, et la température et l'humidité sont lues immédiatement.

Le code configure une interface I2C pour communiquer avec l'écran LCD, spécifiant les broches de données et d'horloge, puis initialise l'écran pour afficher des informations.

Des fonctions sont définies pour chaque note musicale (DO, RE, MI, FA, SOL, LA, SI), permettant de jouer ces notes en réglant la fréquence et le volume du buzzer, puis en jouant la note pendant une durée spécifiée. Une fonction Nope() est aussi incluse pour couper le son.

La fonction BirthdaySong() joue la mélodie de "Joyeux Anniversaire", en appelant les fonctions de note avec des délais pour créer la séquence musicale.

Dans la boucle principale, le script lit régulièrement la température et l'humidité du capteur DHT, affiche ces valeurs sur l'écran LCD, et si la température dépasse 30 degrés ou l'humidité dépasse 45 %, la chanson "Joyeux Anniversaire" est jouée.

Ainsi, ce code combine la lecture de données environnementales avec des capacités sonores, affichant les mesures sur un écran LCD et jouant une mélodie en fonction des conditions ambiantes.
