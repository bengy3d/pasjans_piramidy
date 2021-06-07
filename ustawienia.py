import os

class Ustawienia:
    def __init__(self):
        self.szerokosc_ekranu = 1200
        self.wysokosc_ekranu = 675
        
        self.kolor_tla = (0, 115, 0)
        
        self.szerokosc_karty = 100
        self.wysokosc_karty = 145
        
        self.szerokosc_przycisku = 100
        self.wysokosc_przycisku = 50
        self.kolor_przycisku = (255, 0, 100)
        self.kolor_tekstu = (255, 255, 255)
        
        self.szerokosc_napisu = 200
        self.wysokosc_napisu = 50
        
        self.mozliwe_ruchy = True
        
        #status gry
        self.stan_gry = 0