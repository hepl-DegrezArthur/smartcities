# RGB - SoundSensor
Ce code à pour objectif de faire varier la lumière d'une LED RGB en fonction d'un capteur de son et de lumière.


## Connexions sur Raspberry Pico W
![image](https://github.com/user-attachments/assets/659836fe-fc41-4416-994d-0b89e107374d)


## Explications du code 
La première partie du code importe les bibliothèques nécessaires. La bibliothèque neopixel est utilisée pour contrôler les LEDs NeoPixel, tandis que utime et machine gèrent le temps et les composants matériels (ports GPIO, ADC, etc.).

Ensuite, le code initialise la LED RGB. La variable Led représente le pin connecté à la LED NeoPixel, ici GP18. La variable Neopixel initialise la LED NeoPixel sur ce pin, avec un seul pixel.

Le code définit ensuite plusieurs couleurs en tant que tuples RGB. Par exemple, la couleur rouge est définie comme (255, 0, 0), et blanc comme (255, 255, 255). Ces couleurs sont ensuite stockées dans une liste appelée COLORS.

Le capteur de lumière est initialisé avec la variable Lsensor, utilisant l’entrée analogique ADC(0), et le capteur sonore avec la variable Ssensor, utilisant ADC(1).

La variable Mnoise est initialisée à zéro et sert à stocker une moyenne des valeurs du capteur sonore afin de réduire le bruit aléatoire.

La fonction SensorAverage est définie pour obtenir une moyenne des valeurs lues par le capteur sonore. Elle lit mille valeurs avec une pause d’une microseconde entre chaque lecture, puis elle calcule la moyenne de ces valeurs et la stocke dans la variable Mnoise. Cela permet de réduire le bruit en moyenne sur une série de lectures.

Le bloc while True est une boucle infinie qui exécute en continu le programme. À chaque itération, elle appelle la fonction SensorAverage pour obtenir une moyenne des valeurs du capteur sonore, puis lit la valeur du capteur de lumière avec Lsensor.read_u16().

Si la valeur de lumière est inférieure à 30000 ou que la valeur moyenne du capteur sonore Mnoise dépasse 9000, la LED RGB est allumée en blanc. Sinon, elle est allumée en rouge. La fonction sleep(0.1) introduit une pause de 100 ms entre chaque itération.

En résumé, le programme allume la LED NeoPixel en blanc lorsque le niveau de lumière est faible ou que le bruit dépasse un certain seuil, sinon il allume la LED en rouge.

## FlowChart Diagramme
![image](https://github.com/user-attachments/assets/5669c573-123e-4858-a72b-38ad8c66c982)

