import pygame
import sys

"""Wszystkie funkcje związane z glowna petla gry"""
#petla sprawdzajaca wszystkie wcisniecia i ruchy myszka gracza
def sprawdzanie_wydarzen(pula, piramida, talia, 
                         przycisk_restart, przycisk_menu, strategie, ustawienia, punkty, wskazowka):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #podniesienie karty lub wcisniecie przycisku restart, menu lub zmiana karty w dolnej talii
        elif event.type == pygame.MOUSEBUTTONDOWN:
            przycisk_myszy_dol(event, pula, piramida, talia, 
                               przycisk_restart, przycisk_menu, strategie, ustawienia, punkty, wskazowka)
        #przemieszczanie karty
        elif event.type == pygame.MOUSEMOTION:
            przemieszczanie_karty(event, piramida)
        #upuszczenie karty
        elif event.type == pygame.MOUSEBUTTONUP:
            przycisk_myszy_gora(piramida, talia, strategie, punkty)

def przycisk_myszy_dol(event, pula, piramida, talia, przycisk_restart,
                       przycisk_menu, strategie, ustawienia, punkty, wskazowka):
    piramida.sprawdz_czy_wcisnieto(event)
    war = talia.sprawdz_czy_wcisnieto(event, strategie)
    if war:
        piramida.anuluj_wskazowki()
    wcisniecie_przycisku_restart(event, pula, piramida, talia, 
                                 przycisk_restart, strategie, punkty, ustawienia)
    wcisniecie_przycisku_menu(event, przycisk_menu, ustawienia)
    wcisniecie_przycisku_wskazowka(event, wskazowka, talia, strategie, ustawienia)
    
def przycisk_myszy_gora(piramida, talia, strategie, punkty):
    karta_poruszana = piramida.get_karta_poruszana()
    if karta_poruszana:
        ostatni = talia.znajdz_ostatni()
        #sprawdzenie czy karta polozona na szczytowa karte stosu jest o range mniejsza badz wieksza
        if pygame.sprite.collide_rect(ostatni, karta_poruszana) and (ostatni.ranga - 1 == karta_poruszana.ranga 
                                                                    or ostatni.ranga + 1 == karta_poruszana.ranga):
            talia.usun_karte(ostatni)
            karta_poruszana.zmien_poz_stos()
            talia.dodaj_karte(karta_poruszana)
            piramida.usun_karte(karta_poruszana)
            piramida.odswiez()
            strategie.punkty += 1 * strategie.mnoznik
            punkty.odswiez_punkty()
            strategie.mnoznik += 1
        else:
            karta_poruszana.przywroc_poz()
    
def przemieszczanie_karty(event, piramida):
    karta_poruszana = piramida.get_karta_poruszana()
    if karta_poruszana:
        mysz_x, mysz_y = event.pos
        karta_poruszana.update(mysz_x, mysz_y)

#funkcja wyswietlajaca karty na ekran
def rysuj_ekran(ekran, ustawienia, piramida, talia, przycisk_restart, 
                wygrana, przycisk_menu, punkty, wskazowka, przegrana):
    ekran.fill((ustawienia.kolor_tla))
    #wyswietlanie przyciskow
    przycisk_restart.wyswietl()
    przycisk_menu.wyswietl()
    wskazowka.wyswietl()
    #wyswietlanie punktow
    punkty.wyswietl()
    #wyswietlenie talii i piramidy na ekran
    #talia.stos.draw(ekran)
    #piramida.stos.draw(ekran)
    for karta in talia.stos.sprites():
        karta.blitme()
    for karta in piramida.stos.sprites():
        karta.blitme()
    #wyswietlenie poruszanej karty by zawsze byla widoczna przed innymi kartami
    karta_poruszana = piramida.get_karta_poruszana()
    if karta_poruszana:
        karta_poruszana.blitme()
    if not piramida.stos:
        wygrana.wyswietl()
    if not ustawienia.mozliwe_ruchy and piramida.stos:
        przegrana.wyswietl()
    
    pygame.display.flip()
    
#Funkcja sprawdzjaca czy wcisnieto przycisk restart jesli tak nastepuje zrestartowanie gry
def wcisniecie_przycisku_restart(event, pula, piramida, talia, przycisk_restart,
                                 strategie, punkty, ustawienia):
    if przycisk_restart.rect.collidepoint(event.pos):
        pula.pobierz_zdjecia_z_pliku()
        piramida.restart()
        talia.restart()
        strategie.restart()
        punkty.odswiez_punkty()
        ustawienia.mozliwe_ruchy = True
 
#Funkcja sprawdzajaca czy wcisnieto przycisk menu    
def wcisniecie_przycisku_menu(event, przycisk_menu, ustawienia):
    if przycisk_menu.rect.collidepoint(event.pos):
        ustawienia.stan_gry = 0
        ustawienia.mozliwe_ruchy = True
        
def wcisniecie_przycisku_wskazowka(event, wskazowka, talia, strategie, ustawienia):
    if wskazowka.rect.collidepoint(event.pos):
        karta_t = talia.znajdz_ostatni()
        karta = strategie.sprawdz_warunki(karta_t)
        if karta:
            karta.wskazowka()
        else:
            karta_t = talia.znajdz_przed_ostatni()
            if karta_t:
                karta_t.wskazowka()
            else:
                ustawienia.mozliwe_ruchy = False