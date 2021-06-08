import pygame
from pygame.sprite import Group

class Strategie:
    def __init__(self, piramida, talia):
        self.piramida = piramida
        self.talia = talia
        self.restart()

    def pobierz_liste_kart_widocznych(self):
        self.karty_widoczne = Group()
        for karta in self.piramida.stos.sprites():
            if karta.widocznosc:
                self.karty_widoczne.add(karta)

    def sprawdz_warunki(self, karta_t):
        self.pobierz_liste_kart_widocznych()
        karta_wskazowka = None
        licznik_kart = -1
        for karta in self.karty_widoczne:
            if karta.ranga + 1 == karta_t.ranga or karta.ranga - 1 == karta_t.ranga:
                karty_widoczne_kopia = self.karty_widoczne.copy()
                karty_widoczne_kopia.remove(karta)
                liczba_nastepnych = self.sprawdzanie_nastepnych(karta, karty_widoczne_kopia)
                if licznik_kart < liczba_nastepnych:
                    karta_wskazowka = karta
                    licznik_kart = liczba_nastepnych
                if licznik_kart == liczba_nastepnych:
                    war = self.sprawdzanie_czy_odkrywa()
                    if war:
                        karta_wskazowka = karta
                        licznik_kart = liczba_nastepnych
                        
        return karta_wskazowka
    
    def sprawdzanie_nastepnych(self, karta_t, karty_widoczne):
        najw = 0
        licznik = 0
        for karta in karty_widoczne:
            if karta.ranga + 1 == karta_t.ranga or karta.ranga - 1 == karta_t.ranga:
                licznik = 1
                karty_widoczne_kopia = karty_widoczne.copy()
                karty_widoczne_kopia.remove(karta)
                licznik += self.sprawdzanie_nastepnych(karta, karty_widoczne_kopia)
                if najw < licznik:
                    najw = licznik
                licznik = 0
        if najw == 0:
            return 0
        elif najw != 0:
            return najw
        
    def sprawdzanie_czy_odkrywa(self, karta):
        licznik_pokrytych = 0
        for karta1 in self.piramida.stos.sprites():
            if karta1.msc_w_puli < karta.msc_w_puli and pygame.sprite.collide_rect(karta1, karta):
                licznik_pokrytych += 1
                for karta2 in self.piramida.stos.sprites():
                    if karta1.msc_w_puli < karta2.msc_w_puli and pygame.sprite.collide_rect(karta1, karta2):
                        licznik_pokrytych += 1
                        break
                    break
        if licznik_pokrytych == 1:
            return True
        else:
            return False

    def restart(self):
        self.punkty = 0
        self.mnoznik = 1