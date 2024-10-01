Le code commence par importer des bibliothèques pour interagir avec le matériel et gérer le temps. Ensuite, il définit une broche pour la LED comme sortie et une autre pour le bouton comme entrée, avec une résistance de tirage vers le bas.

Une variable "i" détermine le mode de clignotement de la LED. 

Une fonction de routine d'interruption est définie pour gérer les pressions sur le bouton. À chaque pression, "i" est incrémenté, et lorsque "i" atteint 6, il est réinitialisé à 1, permettant ainsi de passer par différents modes de clignotement.

Une interruption est configurée pour détecter les pressions du bouton. Dans une boucle infinie, le code vérifie la valeur de "i" et fait clignoter la LED de différentes manières selon cette valeur : un clignotement rapide, un clignotement lent, des variations, ou la LED éteinte. Le code commenté à la fin propose une autre méthode de contrôle de la LED, mais celle-ci n'est pas utilisée. En somme, le code ajuste le comportement de la LED en fonction des interactions avec le bouton.

![GPIO](https://github.com/user-attachments/assets/6d0f57e3-f2dd-4e18-b9d9-268e0b32c5d4)