import pygame
from pygame.sprite import Group
from karta import Karta
"""Klasa odpowiadajaca za karty w piramidzie"""
class Piramida:
    def __init__(self, ekran, pula, tryb):
        self.ekran = ekran
        self.pula = pula
        self.tryb = tryb
        self.stos = Group()
        if self.tryb == 1:
            self.buduj_piramide_1()
        else:
            self.buduj_piramidy_2()
            
    #wypelnienie stosu piramidy kartami
    def buduj_piramide_1(self):        
        for i in range(15):
            if i <= 9:
                widocznosc = False
            else:
                widocznosc = True
            nowa_karta = Karta(self.ekran, self.pula, i, widocznosc, self.tryb)
            self.stos.add(nowa_karta)
            
    def buduj_piramidy_2(self):
        for i in range(27):
            if i <= 18:
                widocznosc = False
            else:
                widocznosc = True
            nowa_karta = Karta(self.ekran, self.pula, i, widocznosc, self.tryb)
            self.stos.add(nowa_karta)
    
    #sprawdzenie czy nacisnieto jedna z odkrytych kart        
    def sprawdz_czy_wcisnieto(self, event):
        for karta in self.stos.sprites():
            if karta.widocznosc and karta.rect.collidepoint(event.pos):
                if karta.hint:
                    karta.hint = False
                else:
                    self.anuluj_wskazowki()
                karta.porusza_sie = True
                break
    
    #wydobycie poruszanej karty        
    def get_karta_poruszana(self):
        karta_poruszana = None
    
        for karta in self.stos.sprites():
            if karta.porusza_sie:
                karta_poruszana = karta
                return karta_poruszana
        return False
    
    #usuniecie karty ze stosu piramidy
    def usun_karte(self, karta):
        self.stos.remove(karta)
    
    #odkrywanie kart ktore zostaly odsloniete
    def odswiez(self):
        for karta1 in self.stos.sprites():
            #odslonieta znaczy ze zadna karta nie przykrywa karty
            odslonieta = True
            for karta2 in self.stos.sprites():
                if karta1.msc_w_puli < karta2.msc_w_puli and pygame.sprite.collide_rect(karta1, karta2):
                    odslonieta = False
                    break
            if odslonieta:
                karta1.zmien_widocznosc()
    
    def anuluj_wskazowki(self):
        for karta in self.stos.sprites():
            if karta.hint:
                karta.hint = False
    
    def restart(self):
        self.stos.empty()
        if self.tryb == 1:
            self.buduj_piramide_1()
        else:
            self.buduj_piramidy_2()