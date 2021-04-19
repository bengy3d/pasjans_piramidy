import pygame
from pygame.sprite import Group

import funkcje_gry as fg
from ustawienia import Ustawienia
from pula import Pula
from piramida import Piramida
from talia import Talia
from przycisk import Przycisk

#Funkcja uruchamiajaca gre pasjans
def uruchom_gre():
    pygame.init()
    ustawienia = Ustawienia()
    ekran = pygame.display.set_mode((ustawienia.szerokosc_ekranu, ustawienia.wysokosc_ekranu))
    pula = Pula(ekran, ustawienia, 2)
    pygame.display.set_caption('Pasjans')
    piramida = Piramida(ekran, pula, 2)
    talia = Talia(ekran, pula, 2)
    przycisk_restart = Przycisk(ustawienia, ekran, 'Restart')
    wygrana = Przycisk(ustawienia, ekran, 'WYGRAŁEŚ!')
    wygrana.wysrodkuj()
    #petla gry
    while True:
        fg.sprawdzanie_wydarzen(pula, piramida, talia, przycisk_restart)
        fg.rysuj_ekran(ekran, ustawienia, piramida, talia, przycisk_restart, wygrana)
    
uruchom_gre()