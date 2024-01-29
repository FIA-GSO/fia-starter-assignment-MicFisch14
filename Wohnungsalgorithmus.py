
raumZaehler = 0
wohnungsGroeße = 0
quadratImRaumZaehler= 0
raumAnzahl = int(input("Wie viele Räume sind es? "))

while raumZaehler < raumAnzahl:
    anzahlQuadrate = int(input("Zimmer " + str(raumZaehler+1) +  ": Wie viele Quadrate sind im Raum? "))
    while quadratImRaumZaehler < anzahlQuadrate:
        print("Zimmer " + str(raumZaehler+1) + " - Quadrat " + str(quadratImRaumZaehler+1))
        laenge = int(input("Geben sie die Raumlänge ein "))
        breite = int(input("Geben sie die Breite ein "))
        wohnungsGroeße += laenge * breite
        quadratImRaumZaehler += 1
    quadratImRaumZaehler = 0
    raumZaehler += 1
durchschnittsRaumgroeße = wohnungsGroeße / raumAnzahl
print("Wohnungsgröße: " + str(wohnungsGroeße) + "qm - Durchschnittliche Zimmergröße: " + str(durchschnittsRaumgroeße) + "qm")
