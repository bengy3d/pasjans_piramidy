import pygame

class Przycisk:
    def __init__(self, ustawienia, ekran, tekst):
        self.ekran = ekran
        self.ustawienia = ustawienia
        self.ekran_rect = ekran.get_rect()
        
        self.font = pygame.font.SysFont(None, 35)
        self.rect = pygame.Rect(0, 0, self.ustawienia.szerokosc_przycisku,
                                self.ustawienia.wysokosc_przycisku)
        
        self.rect.top = 30
        self.rect.right = self.ekran_rect.right - 30
        
        self.przygotuj_tekst(tekst)
        
    def przygotuj_tekst(self, tekst):
        self.tekst_zdjecie = self.font.render(tekst, True, 
                                              self.ustawienia.kolor_tekstu, 
                                              self.ustawienia.kolor_przycisku)
        self.tekst_zdjecie_rect = self.tekst_zdjecie.get_rect()
        self.tekst_zdjecie_rect.center = self.rect.center
        
    def komunikat_wygrana(self):
        self.rect = pygame.Rect(0, 0, self.ustawienia.szerokosc_napisu,
                                self.ustawienia.wysokosc_napisu)
        self.rect.center = self.ekran_rect.center
        self.tekst_zdjecie_rect.center = self.rect.center
        
    def menu_glowne(self, nr_przycisku):
        self.rect = pygame.Rect(0, 0, self.ustawienia.szerokosc_napisu,
                                self.ustawienia.wysokosc_napisu)
        if nr_przycisku == 1:
            self.rect.center = self.ekran_rect.center
        elif nr_przycisku == 2:
            self.rect.center = self.ekran_rect.center
            self.rect.y += 100
        else:
            self.rect.center = self.ekran_rect.center
            self.rect.y -= 100
        self.tekst_zdjecie_rect.center = self.rect.center
        
    def wyswietl(self):
        self.ekran.fill(self.ustawienia.kolor_przycisku, self.rect)
        self.ekran.blit(self.tekst_zdjecie, self.tekst_zdjecie_rect)
        