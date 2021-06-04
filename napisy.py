import pygame.font

class Napisy:
    
    def __init__(self, ekran, ustawienia, napis):
        self.ekran = ekran
        self.ekran_rect = ekran.get_rect()
        self.ustawienia = ustawienia
        self.font = pygame.font.SysFont(None, 48)
        
        self.kolor_tekstu = (255, 255, 255)
        self.przygotuj_tekst(napis)
        
    def przygotuj_tekst(self, napis):
        self.napis_zdjecie = self.font.render(napis, True, self.kolor_tekstu,
                                              self.ustawienia.kolor_tla)
        self.napis_rect = self.napis_zdjecie.get_rect()
        self.napis_rect.center = self.ekran_rect.center
        self.napis_rect.y -= 100
        
    def wyswietl(self):
        self.ekran.blit(self.napis_zdjecie, self.napis_rect)
        
        

