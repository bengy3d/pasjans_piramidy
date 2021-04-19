import pygame
import sys

"""Wszystkie funkcje związane z glowna petla gry"""
#petla sprawdzajaca wszystkie wcisniecia i ruchy myszka gracza
def sprawdzanie_wydarzen(pula, piramida, talia, przycisk_restart):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #podniesienie karty
        elif event.type == pygame.MOUSEBUTTONDOWN:
            piramida.sprawdz_czy_wcisnieto(event)
            talia.sprawdz_czy_wcisnieto(event)
            wcisniecie_przycisku(event, pula, piramida, talia, przycisk_restart)
        #przemieszczanie karty
        elif event.type == pygame.MOUSEMOTION:
            karta_poruszana = piramida.get_karta_poruszana()
            if karta_poruszana:
                mysz_x, mysz_y = event.pos
                karta_poruszana.update(mysz_x, mysz_y)
        #upuszczenie karty
        elif event.type == pygame.MOUSEBUTTONUP:
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
                else:
                    karta_poruszana.przywroc_poz()

#funkcja wyswietlajaca karty na ekran
def rysuj_ekran(ekran, ustawienia, piramida, talia, przycisk_restart, wygrana):
    ekran.fill((ustawienia.kolor_tla))
    przycisk_restart.wyswietl()
    karta_poruszana = piramida.get_karta_poruszana()
    #wyswietlenie talii i piramidy na ekran
    talia.stos.draw(ekran)
    piramida.stos.draw(ekran)
    #wyswietlenie poruszanej karty by zawsze byla widoczna przed innymi kartami
    karta_poruszana = piramida.get_karta_poruszana()
    if karta_poruszana:
        karta_poruszana.blitme()
    if not piramida.stos:
        wygrana.wyswietl()
    
    pygame.display.flip()
    
#Funkcja sprawdzjaca czy wcisnieto przycisk restart jesli tak nastepuje zrestartowanie gry
def wcisniecie_przycisku(event, pula, piramida, talia, przycisk_restart):
    if przycisk_restart.rect.collidepoint(event.pos):
        pula.pobierz_zdjecia_z_pliku()
        piramida.restart()
        talia.restart()