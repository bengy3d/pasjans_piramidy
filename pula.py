import os

class Pula:
    def __init__(self, ekran, ustawienia, tryb):
        self.ekran_rect = ekran.get_rect()
        self.pobierz_zdjecia_z_pliku()
        self.tryb = tryb
        
        self.piramida_kart = []
        centerx = self.ekran_rect.centerx
        top = self.ekran_rect.top + 20
        szerokosc = ustawienia.szerokosc_karty
        if tryb == 1:
            #petla wypelniajaca liste pozycji kart w piramidzie
            for i in range(5):
                x = centerx - i * (szerokosc * 0.75)
                y = top + i * (ustawienia.wysokosc_karty / 2)
                self.piramida_kart.append((x, y))
                if i != 0:
                    for j in range(i):
                        x += szerokosc * 0.75 * 2
                        self.piramida_kart.append((x, y))
        else:
            #Wywolanie wartosci x kart poczatkowych w dwoch piramidach
            centerx1 = self.ekran_rect.centerx - szerokosc * 2.25
            centerx2 = self.ekran_rect.centerx + szerokosc * 2.25
            # Petla wypelniajaca liste pozycji kart w dwoch piramidach
            for i in range(3):
                x1 = centerx1 - i * (szerokosc * 0.75)
                x2 = centerx2 - i * (szerokosc * 0.75)
                y = top + i * (ustawienia.wysokosc_karty / 2)
                self.piramida_kart.append((x1, y))
                self.piramida_kart.append((x2, y))
                if i != 0:
                    for j in range(i):
                        x1 += szerokosc * 0.75 * 2
                        x2 += szerokosc * 0.75 * 2
                        self.piramida_kart.append((x1, y))
                        self.piramida_kart.append((x2, y))
            #Pobranie wspolrzednej x, y kart w ostatnim rzedzie
            licznik = 6
            for i in range(3, 5):
                y = top + i * (ustawienia.wysokosc_karty / 2)
                x = centerx1 - i * (szerokosc * 0.75)
                self.piramida_kart.append((x, y))
                #Petla wypelniajaca ostatni rzad piramidy
                for j in range(licznik):
                    x += szerokosc * 0.75 * 2
                    self.piramida_kart.append((x, y))
                licznik += 1
        
        pom = len(self.piramida_kart)
        
        x, y = self.piramida_kart[pom - 1]
        #pozycja kart zakrytych w talii            
        self.poz_stos_zakryty = (centerx - 0.75 * szerokosc, 
                                 y + 1.25 * ustawienia.wysokosc_karty)
        #pozycja karty odkrytej w talii
        self.poz_stos_otwarty = (centerx + 0.75 * szerokosc, 
                                 y + 1.25 * ustawienia.wysokosc_karty)
        
    #pobranie nazw zdjec odkrytych kart z folderu ze zdjeciami
    def pobierz_zdjecia_z_pliku(self):
        sciezka = 'zdjecia_otwartych/'
        self.zdjecia_otwartych = [os.path.join(sciezka, file)
                                for file in os.listdir(sciezka)
                                if file.endswith('.bmp')]