import pygame.font

class Punkty:
    
    def __init__(self, ekran, ustawienia, strategie):
        self.ekran = ekran
        self.ekran_rect = ekran.get_rect()
        self.ustawienia = ustawienia
        self.strategie = strategie
        
        self.kolor_tekstu = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.odswiez_punkty()
        
    def odswiez_punkty(self):
        punkty_str = str(self.strategie.punkty)
        punkty_str = 'Punkty: ' + punkty_str
        self.punkty_zdjecie = self.font.render(punkty_str, True, self.kolor_tekstu,
                                               self.ustawienia.kolor_tla)
        self.punkty_rect = self.punkty_zdjecie.get_rect()
        self.punkty_rect.bottom = self.ekran_rect.bottom - 20
        self.punkty_rect.right = self.ekran_rect.right - 20
    
    def wyswietl(self):
        self.ekran.blit(self.punkty_zdjecie, self.punkty_rect)