import pygame
from pygame.sprite import Group

import menu_glowne as mg
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
    pygame.display.set_caption('Pasjans')
    tekst_wyboru = Przycisk(ustawienia, ekran, 'Wybierz tryb:')
    tekst_wyboru.menu_glowne(3)
    przycisk_menu_1 = Przycisk(ustawienia, ekran, '1 piramida')
    przycisk_menu_1.menu_glowne(1)
    przycisk_menu_2 = Przycisk(ustawienia, ekran, '2 piramidy')
    przycisk_menu_2.menu_glowne(2)
    #petla menu glownego gry
    while True:
        wybor = mg.sprawdzanie_wydarzen(przycisk_menu_1, przycisk_menu_2)
        mg.rysuj_ekran(ekran, ustawienia, przycisk_menu_1, przycisk_menu_2, tekst_wyboru)
        if wybor != 0:
            break
        
    pula = Pula(ekran, ustawienia, wybor)
    piramida = Piramida(ekran, pula, wybor)
    talia = Talia(ekran, pula, wybor)
    przycisk_restart = Przycisk(ustawienia, ekran, 'Restart')
    wygrana = Przycisk(ustawienia, ekran, 'WYGRAŁEŚ!')
    wygrana.komunikat_wygrana()
    #petla gry
    while True:
        fg.sprawdzanie_wydarzen(pula, piramida, talia, przycisk_restart)
        fg.rysuj_ekran(ekran, ustawienia, piramida, talia, przycisk_restart, wygrana)
    
uruchom_gre()