# -*- coding: utf-8 -*-
#Import required libraries:
import turtle
import random
import matplotlib.pyplot as plt
import math


#Functions:
def narysujOkrag(narzedzieRysujace, radius):
  narzedzieRysujace.up()
  narzedzieRysujace.right(90)
  narzedzieRysujace.forward(radius)
  narzedzieRysujace.left(90)
  narzedzieRysujace.down()
  narzedzieRysujace.circle(radius)
  narzedzieRysujace.up()
  narzedzieRysujace.left(90)
  narzedzieRysujace.forward(radius)
  narzedzieRysujace.right(90)

def narysujKwadrat(narzedzieRysujace, bok):
  narzedzieRysujace.up()
  narzedzieRysujace.forward(bok/2)
  narzedzieRysujace.left(90)
  narzedzieRysujace.forward(bok/2)
  narzedzieRysujace.down()
  for j in range(4):
      narzedzieRysujace.left(90)
      narzedzieRysujace.forward(bok)
  narzedzieRysujace.up()
  narzedzieRysujace.back(bok/2)
  narzedzieRysujace.right(90)
  narzedzieRysujace.back(bok/2)
       

class Punkt3D:
    def __init__(self, x=0, y=0, z=0):
      self.x = x
      self.y = y
      self.z = z
    
    def print(self):
        print("(x={0}, y={1}, z={2})".format(self.x, self.y, self.z))
    
    def odlegloscOdPunktu(self, drugiPunkt3D):
        return math.sqrt(math.pow((self.x - drugiPunkt3D.x), 2) 
                         + math.pow((self.y - drugiPunkt3D.y), 2) 
                         + math.pow((self.z - drugiPunkt3D.z), 2))
    
    def narysujOdpowiadajacaKropke(self, narzedzieRysujace, kolor):
        narzedzieRysujace.color(kolor)
        narzedzieRysujace.up()
        narzedzieRysujace.setposition(self.x, self.y)
        narzedzieRysujace.up()
        narzedzieRysujace.dot()
        narzedzieRysujace.up()
        narzedzieRysujace.color("black")
        
        
#Variables:
przykladowaKula_promien = 300
punktStartu = Punkt3D(0,0,0)
iloscProbek = 3000
coIleProbekInfo = 500
czyRysowacPunkty = False   

przykladowySzescian_bok = 300*2
stosunekObjKuliToObjSzescianu = math.pi/6

#Main:

#Draw orange cross-section    
kredka = turtle.Turtle()
kredka.hideturtle()
kredka.up()
kredka.setposition(punktStartu.x, punktStartu.y)
kredka.speed(0)
narysujOkrag(kredka, przykladowaKula_promien)
narysujKwadrat(kredka, przykladowySzescian_bok)

#Print work data
print('Promien kuli wpisanej: {0}, bok szescianu opisanego: {1}'.format(przykladowaKula_promien, przykladowySzescian_bok))
print('Stosunek objetosci kuli do objetosci szescianu ze wzoru: ' + str(stosunekObjKuliToObjSzescianu))

#Calculating approximates:
licznik_wKuli = 0
licznik_wPozaKula = 0

oszaczowaniaStosunkuObj = []

print("Rozpoczecie estymacji: ")
for i in range(iloscProbek):
    x = random.randrange(-przykladowaKula_promien, przykladowaKula_promien)
    y = random.randrange(-przykladowaKula_promien, przykladowaKula_promien)
    z = random.randrange(-przykladowaKula_promien, przykladowaKula_promien)
    
    losowyPunkt = Punkt3D(x,y,z)
    odlegloscLosowegoPunktuOdStartu = losowyPunkt.odlegloscOdPunktu(punktStartu)
    if (odlegloscLosowegoPunktuOdStartu <= przykladowaKula_promien):
        if(czyRysowacPunkty):
            losowyPunkt.narysujOdpowiadajacaKropke(kredka, "red")
        licznik_wKuli = licznik_wKuli+1
    else:
        if(czyRysowacPunkty):
            losowyPunkt.narysujOdpowiadajacaKropke(kredka, "black")
        licznik_wPozaKula = licznik_wPozaKula+1
     
    #print(str(licznik_wKuli) + " " + str(licznik_wPozaKula))
    if(licznik_wKuli == 0 or licznik_wPozaKula == 0):
        oszacowanieStosunkuObjDlaKroku = 0 
    else:
        oszacowanieStosunkuObjDlaKroku = licznik_wKuli/(licznik_wKuli+licznik_wPozaKula)
    
    oszaczowaniaStosunkuObj.append(oszacowanieStosunkuObjDlaKroku)
    
    if(i%coIleProbekInfo == 0):
        print("   Krok i={0}, wartosc estymacji: {1}".format(i,oszacowanieStosunkuObjDlaKroku))

print("Koniec estymacji.")

bledyDlaOszacowan = [abs(stosunekObjKuliToObjSzescianu - ratio) for ratio in oszaczowaniaStosunkuObj]

# Print results
print('Koncowa wyestymowana wartosc stosunku objetosci kuli do objetosci szescianu: ' + str(oszaczowaniaStosunkuObj[-1]))

#Ploting data
plt.axhline(y=stosunekObjKuliToObjSzescianu, color='g', linestyle='-')
plt.plot(oszaczowaniaStosunkuObj)
plt.xlabel("Ilosc iteracji")
plt.ylabel("Wartosc proporcji Vk/Vsz")
plt.show()

plt.axhline(y=0.0, color='g', linestyle='-')
plt.plot(bledyDlaOszacowan)
plt.xlabel("Ilosc iteracji")
plt.ylabel("Odchylenie od oczekiwanej wartoci")
plt.show()

#end Main
turtle.done()
try:
    turtle.bye()   
except turtle.Terminator:
    pass



