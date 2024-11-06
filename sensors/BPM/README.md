# RGB - SoundSensor
Ce code a pour but de détecter le bpm d'une musique à l'aide d'un capteur de son. Il modifie ensuite la couleur d'une LED RGB afin de montrer lorsqu'un battement a été interrprêté.


## Connexions sur Raspberry Pico W



## Explications du code 
La première partie du code importe les bibliothèques nécessaires. La bibliothèque neopixel permet de contrôler la LED NeoPixel, utime et machine sont utilisées pour la gestion du temps et des composants matériels (broches GPIO, ADC, etc.), et random est utilisée pour sélectionner une couleur aléatoire.

Ensuite, la LED RGB est initialisée sur la broche GP18, et un seul pixel est configuré pour le NeoPixel. Le code définit ensuite plusieurs couleurs en tuples RGB, par exemple le rouge est représenté par (255, 0, 0) et le blanc par (255, 255, 255). Ces couleurs sont stockées dans une liste appelée colors, qui servira pour choisir une couleur aléatoire à chaque battement détecté.

Le capteur sonore est initialisé avec la variable Ssensor, utilisant l’entrée analogique ADC(1). Deux variables sont définies : RefNoise pour stocker la valeur de référence du bruit ambiant, et Vbattement, un seuil de bruit utilisé pour détecter un battement. La variable LastTime est initialisée avec le temps actuel en millisecondes, elle servira à mesurer le temps écoulé entre deux battements.

La fonction SoundSensorAverage est définie pour obtenir une moyenne de bruit en faisant 1000 lectures du capteur sonore avec une pause d’une microseconde entre chaque lecture. La moyenne obtenue est retournée pour réduire les variations rapides dans les mesures.

Dans la boucle principale infinie, le code utilise la fonction SoundSensorAverage pour obtenir une moyenne de bruit. Il compare ensuite cette valeur avec RefNoise pour voir si le changement dépasse le seuil Vbattement. Si c’est le cas, un battement est détecté, et le code capture le temps actuel en millisecondes dans CurrentTime. Il calcule ensuite le temps écoulé depuis le dernier battement, stocké dans VTime. Si ce délai est supérieur à 300 ms (pour éviter les détections multiples causées par les sons parasites), le code calcule la fréquence cardiaque en BPM comme 60000 divisé par VTime et affiche le résultat.

Une couleur aléatoire est alors choisie dans la liste colors et appliquée à la LED NeoPixel pour signaler visuellement le battement. La valeur de RefNoise est mise à jour avec la valeur de bruit actuelle, et le programme attend 50 ms avant de reprendre la boucle, permettant ainsi des pauses entre chaque détection de battement.

## FlowChart Diagramme



