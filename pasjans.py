import pygame

import menu_glowne as mg
import funkcje_gry as fg
from ustawienia import Ustawienia
from pula import Pula
from piramida import Piramida
from talia import Talia
from przycisk import Przycisk
from napisy import Napisy
from strategie import Strategie
from punkty import Punkty

#Funkcja uruchamiajaca gre pasjans
def uruchom_gre():
    pygame.init()
    ustawienia = Ustawienia()
    ekran = pygame.display.set_mode((ustawienia.szerokosc_ekranu, ustawienia.wysokosc_ekranu))
    pygame.display.set_caption('Pasjans')
    #przyciski i komunikaty
    tekst_wyboru = Napisy(ekran, ustawienia, 'Wybierz tryb')
    przycisk_menu_1 = Przycisk(ustawienia, ekran, '1 piramida')
    przycisk_menu_1.menu_glowne(1)
    przycisk_menu_2 = Przycisk(ustawienia, ekran, '2 piramidy')
    przycisk_menu_2.menu_glowne(2)
    #petla menu glownego gry
    while True:
        while True:
            mg.sprawdzanie_wydarzen(przycisk_menu_1, przycisk_menu_2, ustawienia)
            mg.rysuj_ekran(ekran, ustawienia, przycisk_menu_1, przycisk_menu_2, tekst_wyboru)
            if ustawienia.stan_gry != 0:
                break
        #zmienne do gry
        pula = Pula(ekran, ustawienia, ustawienia.stan_gry)
        piramida = Piramida(ekran, pula, ustawienia.stan_gry)
        talia = Talia(ekran, pula, ustawienia.stan_gry)
        przycisk_restart = Przycisk(ustawienia, ekran, 'Restart')
        wygrana = Napisy(ekran, ustawienia, 'WYGRALES!')
        wygrana.wysrodkuj()
        przegrana = Napisy(ekran, ustawienia, 'Niestety przegrales sprobuj ponownie')
        przegrana.wysrodkuj()
        przycisk_menu = Przycisk(ustawienia, ekran, 'Menu glowne')
        przycisk_menu.menu_glowne(3)
        wskazowka = Przycisk(ustawienia, ekran, 'Wskazowka')
        wskazowka.menu_glowne(4)
        strategie = Strategie(piramida,talia)
        punkty = Punkty(ekran, ustawienia, strategie)
        #petla gry
        while True:
            fg.sprawdzanie_wydarzen(pula, piramida, talia, 
                                    przycisk_restart, przycisk_menu, 
                                    strategie, ustawienia, punkty, wskazowka)
            fg.rysuj_ekran(ekran, ustawienia, piramida, talia, przycisk_restart, 
                           wygrana, przycisk_menu, punkty, wskazowka, przegrana)
            if ustawienia.stan_gry == 0:
                break
    
uruchom_gre()