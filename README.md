# Music_Player

![image](https://user-images.githubusercontent.com/87471423/129364714-6f793126-5863-4c54-8387-1377ddbe423d.png)

Ein Musik Player für die Pixel Boy App

# Aussehen
![image](https://user-images.githubusercontent.com/87471423/129363809-1c27f8c0-359d-4512-b7f8-c54a90f07985.png)

# Funktionen:
    o Abspielen von Musik am PC oder wenn verbunden automatisch am Pixel-Boy
    o Die Verbindug zum Pixel-Boy verwendet das im Osi Layer 2 Protokoll sprich Mac-Adressen
      -> Vorteil: Es kann gleichzeitig Musik abgespielt und den Pixel-Boy Daten gesendet werden,
                  ohne die Übertragungsgeschwindigkeit zu beeinflussen!
    o Automatische Suche nach Liedern
    o Automatisch abspielen des nächsten Liedes, wenn das vorhergehende endet
    o Animierter Text zur Darstellung des gesamten Titles

# Benötigte Librarys:
    o Ctkinter:       -> Wird für alle Objekte am Media Player benötigt -> Vorteil von Runden und moderner Optik
                      -> Beschreibung unter follgendem Link: https://github.com/Diplomarbeit-Datenbank/Ctkinter
    o pygame:         -> Für das abspielen von MP3-Datein
                      -> pip install pygame
    o Encode_Umlauts: -> Wird verwendet um Umlaute richtig darzustellen
                      -> Beschreibung unter follgendem Link: https://github.com/Diplomarbeit-Datenbank/Encode_Umlauts
    o glob:           -> Um alle MP3-Dateien in einem OS-Ordner zu finden
                      -> pip install golob
                 

# Benutzer Verwendung:
![image](https://user-images.githubusercontent.com/87471423/129366157-3b8510a1-013c-4314-a305-7d9ad0fbe20f.png)

# Entwickler Verwendung:
    -> Dieses stand-alone Programm benötigt keine zusätzliche programmierung, es kann einfach am Interface plaziert werden
    -> Sollten doch änderungen wie zum Beispiel Farben durchgeführt werden ist dies in Python-Syntax zu vollziehen

# Eigenschaften:
    o Copyright Christof Haidegger 
    o Erstellt von Christof Haidegger
    o Debugging von Christof Haidegger
    
    o Geschriebende Zeilen in Python-Code : 472
    o Geschriebene Zeilen REDME-Code: 44
