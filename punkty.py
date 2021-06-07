import pygame.font
from os import path

class Punkty:
    
    def __init__(self, ekran, ustawienia, strategie):
        self.ekran = ekran
        self.ekran_rect = ekran.get_rect()
        self.ustawienia = ustawienia
        self.strategie = strategie
        
        self.kolor_tekstu = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
    def odswiez_punkty(self):
        punkty_str = str(self.strategie.punkty)
        punkty_str = 'Punkty: ' + punkty_str
        self.punkty_zdjecie = self.font.render(punkty_str, True, self.kolor_tekstu,
                                               self.ustawienia.kolor_tla)
        self.punkty_rect = self.punkty_zdjecie.get_rect()
        self.punkty_rect.bottom = self.ekran_rect.bottom - 20
        self.punkty_rect.right = self.ekran_rect.right - 20
        
    def odswiez_rekord(self):
        if not path.isfile('rekord.txt'):
            with open('rekord.txt', 'w') as f:
                f.write('0\n0')
        self.pobierz_rekordy_z_pliku()
        if self.ustawienia.stan_gry == 1:
            rekord = self.rekord1
        else:
            rekord = self.rekord2
        rekord_str = 'Rekord: ' + rekord.strip()
        self.punkty_zdjecie = self.font.render(rekord_str, True, self.kolor_tekstu,
                                               self.ustawienia.kolor_tla)
        self.punkty_rect = self.punkty_zdjecie.get_rect()
        self.punkty_rect.bottom = self.ekran_rect.bottom - 100
        self.punkty_rect.right = self.ekran_rect.right - 20
    
    def pobierz_rekordy_z_pliku(self):
        with open('rekord.txt', 'r') as f:
            self.rekord1 = f.readline()
            self.rekord2 = f.readline()
        
    def zapisz_rekord(self):
        self.pobierz_rekordy_z_pliku()
        self.ustawienia.zapis_do_pliku = True
        with open('rekord.txt', 'w') as f:
            if self.ustawienia.stan_gry == 1:
                f.write(str(self.strategie.punkty) + '\n' + str(self.rekord2))
            else:
                f.write(str(self.rekord1) + '\n' + str(self.strategie.punkty))
    
    def wyswietl(self):
        self.ekran.blit(self.punkty_zdjecie, self.punkty_rect)