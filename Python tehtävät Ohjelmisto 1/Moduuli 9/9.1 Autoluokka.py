'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta
pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.'''

class Auto:

    määrä = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

        Auto.määrä += 1

    def tiedot(self):

        tieto = [self.rekisteritunnus,
                  self.huippunopeus,
                  self.nopeus,
                  self.matka]

        return tieto



auto1 = Auto("ABC-123", 142)



# testejä
# print(auto1.rekisteritunnus)
# print(Auto.määrä)

# palautetaan tiedot listaan huvin vuoksi

tieto_lista = auto1.tiedot()
print(f"Rekisteritunnus: {tieto_lista[0]} \nHuippunopeus: {tieto_lista[1]}km/h \nNopeus: {tieto_lista[2]}km/h \nKuljettu matka: {tieto_lista[3]}km \n")

