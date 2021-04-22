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
        przycisk_menu = Przycisk(ustawienia, ekran, 'Menu glowne')
        przycisk_menu.menu_glowne(4)
        #petla gry
        while True:
            war = fg.sprawdzanie_wydarzen(pula, piramida, talia, przycisk_restart, przycisk_menu)
            fg.rysuj_ekran(ekran, ustawienia, piramida, talia, przycisk_restart, wygrana, przycisk_menu)
            if war:
                break
    
uruchom_gre()