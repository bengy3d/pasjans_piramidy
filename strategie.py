from pygame.sprite import Group

class Strategie:
    def __init__(self, piramida, talia):
        self.piramida = piramida
        self.talia = talia
        self.restart()

    def restart(self):
        self.slownik = {liczba: 0 for liczba in range(1, 14)}
        for karta in self.piramida.stos.sprites():
            if karta.widocznosc:
                self.slownik[karta.ranga] += 1
        #z talii kart dolnych
        for karta in self.talia.stos.sprites():
            if karta.widocznosc:
                self.slownik[karta.ranga] += 1
                
        self.punkty = 0
        self.mnoznik = 1