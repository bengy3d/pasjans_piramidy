import pygame
import sys

def sprawdzanie_wydarzen(przycisk_menu_1, przycisk_menu_2, ustawienia):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            wcisniecie_przycisku(event, przycisk_menu_1, przycisk_menu_2, ustawienia)
    
def rysuj_ekran(ekran, ustawienia, przycisk_menu_1, przycisk_menu_2, tekst_wyboru):
    ekran.fill((ustawienia.kolor_tla))
    tekst_wyboru.wyswietl()
    przycisk_menu_1.wyswietl()
    przycisk_menu_2.wyswietl()
    pygame.display.flip()
    
def wcisniecie_przycisku(event, przycisk_menu_1, przycisk_menu_2, ustawienia):
    if przycisk_menu_1.rect.collidepoint(event.pos):
        ustawienia.stan_gry = 1
    elif przycisk_menu_2.rect.collidepoint(event.pos):
        ustawienia.stan_gry = 2
        