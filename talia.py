from pygame.sprite import Group

from karta import Karta

"""Klasa odpowiadajaca za karty w dolnej talii kart"""
class Talia:
    #wypelnienie stosu kartami
    def __init__(self, ekran, pula, tryb):
        self.tryb = tryb
        self.stos = Group()
        self.ekran = ekran
        self.pula = pula
        self.wypelnij_talie()
                
    def wypelnij_talie(self):
        koniec = len(self.pula.zdjecia_otwartych)
        if self.tryb == 1:
            licznik = 15
        else:
            licznik = 27
        for i in range(koniec):
            if i != (koniec - 1):
                nowa_karta = Karta(self.ekran, self.pula, licznik, False, self.tryb)
                self.stos.add(nowa_karta)
                licznik += 1
            else:
                nowa_karta = Karta(self.ekran, self.pula, licznik, True, self.tryb)
                self.stos.add(nowa_karta)
                
    #wydobycie ostatniego elementu w stosie
    def znajdz_ostatni(self):
        ostatni = None
        for karta in self.stos.sprites():
            ostatni = karta
        return ostatni
    
    def znajdz_przed_ostatni(self):
        przed_ostatni = None
        for karta in self.stos.sprites():
            if not karta.widocznosc:
                przed_ostatni = karta
        return przed_ostatni
    
    #sprawdzenie czy uzytkownik wcisnal karte jesli tak to ustawienie nowej na szczycie stosu    
    def sprawdz_czy_wcisnieto(self, event, strategie):
        for karta in self.stos.sprites():
            if not karta.widocznosc and karta.rect.collidepoint(event.pos) and karta.rysuj:
                ostatni = self.znajdz_ostatni()
                self.stos.remove(ostatni)
                ostatni = self.znajdz_ostatni()
                ostatni.zmien_poz_stos()
                ostatni.zmien_widocznosc()
                strategie.mnoznik = 1
                """ Warunek sprawdzajacy czy dlugosc stosu jest wieksza od 1 jesli tak 
                    program szuka przed ostatniej karty w stosie i sprawia ze zostaje
                    ona wypisana na ekran w swoim stanie widocznosci """
                if len(self.stos) > 1:
                    przed_ostatni = self.znajdz_przed_ostatni()
                    przed_ostatni.zmien_wyswietlanie()
                if karta.hint:
                    karta.hint = False
                return True
    
    #usuniecie karty ze stosu
    def usun_karte(self, karta):
        self.stos.remove(karta)
    
    #dodanie karty do stosu    
    def dodaj_karte(self, karta):
        self.stos.add(karta)
    
    #oproznienie talii i ponowne jej wypelnienie    
    def restart(self):
        self.stos.empty()
        self.wypelnij_talie()    