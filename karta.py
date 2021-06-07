import pygame
from random import randint
from pygame.sprite import Sprite
from time import sleep
"""Klasa przechowujaca dane na temat kart i wszystkie ich metody"""
class Karta(Sprite):
    def __init__(self, ekran, pula, msc_w_puli, widocznosc, tryb):
        super().__init__()
        self.tryb = tryb
        self.widocznosc = widocznosc
        self.pula = pula
        self.rysuj = True
        self.ekran = ekran
        self.ekran_rect = ekran.get_rect()
        self.msc_w_puli = msc_w_puli
        self.hint = False
        
        numer = randint(0, len(pula.zdjecia_otwartych) - 1)
        
        self.nazwa = pula.zdjecia_otwartych[numer]
        pula.zdjecia_otwartych.pop(numer)
        
        if self.widocznosc:
            self.image = pygame.image.load(self.nazwa)
        else:
            self.image = pygame.image.load('zdjecia_zakrytych/back_black.bmp')
            
        nazwa_karty = self.nazwa.replace('.bmp', '')
        nazwa_karty = nazwa_karty.replace('zdjecia_otwartych/', '')
        nazwa_karty = nazwa_karty.split('_')
        
        self.kolor = nazwa_karty[0]
        self.ranga = int(nazwa_karty[1])
        
        if self.tryb == 1:
            self.rozmiar_piramidy = 15
        else:
            self.rozmiar_piramidy = 27
        
        self.rozdawanie_pozycji()
        
        self.rect = self.image.get_rect()
        self.przywroc_poz()
    
    def rozdawanie_pozycji(self):
        if self.msc_w_puli < self.rozmiar_piramidy:
            self.x, self.y = self.pula.piramida_kart[self.msc_w_puli]
        elif self.msc_w_puli >= self.rozmiar_piramidy and self.msc_w_puli < 51:
            self.rysuj = False
            self.x, self.y = self.pula.poz_stos_zakryty
            if self.msc_w_puli == 50:
                self.rysuj = True
        elif self.msc_w_puli == 51:
            self.x, self.y = self.pula.poz_stos_otwarty
        
    #Odswiezenie pozycji karty na podstawie ruchu myszka
    def update(self, mysz_x, mysz_y):
        if mysz_x >= 50 and mysz_x <= self.ekran_rect.right - 50:
            self.rect.centerx = mysz_x
        if mysz_y >= 73 and mysz_y <= self.ekran_rect.bottom - 73:
            self.rect.centery = mysz_y
    
    #zmiana widocznosci karty w piramidzie       
    def zmien_widocznosc(self):
        self.widocznosc = True
        self.image = pygame.image.load(self.nazwa)
        self.rect = self.image.get_rect()
        self.przywroc_poz()
    
    #zmiana pozycji karty w talii    
    def zmien_poz_stos(self):
        self.x, self.y = self.pula.poz_stos_otwarty
        self.rect.centerx = self.x
        self.rect.y = self.y
    
    #przywrocenie pozycji karty w piramidzie        
    def przywroc_poz(self):
        self.porusza_sie = False
        self.rect.centerx = self.x
        self.rect.y = self.y
    
    #Zmiana wyswietlania kart w talii    
    def zmien_wyswietlanie(self):
        if self.rysuj:
            self.rysuj = False
        else:
            self.rysuj = True
            
    def wskazowka(self):
        self.zdjecie_wskazowki = pygame.image.load('zdjecia_zakrytych/ramka.bmp')
        self.hint = True
    
    #wyswietlenie karty na ekran        
    def blitme(self):
        self.ekran.blit(self.image, self.rect)
        if self.hint:
            self.ekran.blit(self.zdjecie_wskazowki, self.rect)