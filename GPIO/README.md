About RPI Pico W ...

Afin de prendre en main l'utilisation d'un RPI Pico W et sa programmation en uPython, ces quelques tâches ont étés réalisées : 

- Installation de la dernière mise à jour du fichier uPython dans le RPI
- Prise en main du logiciel Thonny
- Contrôle d'une LED
- Contrôle d'un bouton poussoir
- Utilisation d'un bouton poussoir et d'une LED en même temps avec différents programmes

Explications du code : 
-  Dans un premier temps je commence ar importer la librairie machine qui sera nécéssaire pour pouvoir contrôler l'hardware. J'importe aussi la librairie "utime" afin de pouvoir utiliser une fonction de temps (faire des pauses etc).
-  Ensuite je définis une instance "LED" qui permettra d'agir sur la pin extérieur ou est branchée la LED. Il a été nécéssaire d'entrér plusieurs paramètre comme le numéro de la PIN et si la pin est en sorte ou en entrée. Je fais de même avec une instance Button pour l'utilisation d'un bouton poussoir.
-  Je définis ensuite une variable "count" qui va me permettre de savoir quand on a appuyer sur le bouton et maitenir l'état de la LED.
-  Le code principal se trouve dans une boucle while afin qu'il troune en boucle
-  On commmence par vérifier si le bouton est appuyé, si oui la variable count est incrémentée.
-  Si on appuie de nouveau sur le boutton poussoir, la variable sera incrémentée à 2 mais sera rénitialisée par le elif qui suit.
-  L'état de la varialbe count (1 ou 0) défini l'état de la LED.
 Cette méthode permet que lorsque le bouton est appuyé, la LED s'allume. Si il est à nouveau appuyé, la LED s'éteint et ainsi de suite. 


  ![image](https://github.com/user-attachments/assets/b5f0d874-1e4e-4ab2-a0d9-b97be2b2b8e3)
