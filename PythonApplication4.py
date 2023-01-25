#10-----------------

from math import *

print("Ajateisendus")

V=float(input("sisesta aja minutites: "))

t=int(V//60)

sec=int(V%60)

print(f"minutes {t}: sekundid {sec}")

#9-------------

from math import *

print("Rulluisutajad")

print("Rulluisutaja keskmine kiirus on 29,9km/h")

m=24/60

t=m*29.9

t=round(t,2)

print(f"Vastus: {t}km")

print()

#8--------------
from math import *

print("kütusekulu arvutamine")

l=float(input("kasutaja sisestab tangitud kütuse liitrid: "))

km=float(input("kasutaja sisestab läbitud kilomeetrid: "))

p=l/km*100

print (f"Vastus: {p}l/km")

print()
#7--------------
from math import *

print("Pitsa Võtsite 3 sõbraga suure pitsa hinnaga 12,90€ te jätate teenindajal")

s=10*12.90/100

s=round(s)

d=(12.90+s)

p=d/3

p=round(p,1)

print (f" Iga sõber peab maksma: {p}€")

print()
#6--------------
from math import *
from random import *
a=randint (1,100)
b=randint (1,100)
c=randint (1,100)
print(f"külg a={a}/nKülg b={b}/ nkülg c={c}")
print(f"kolmnurga ümbermõõt = {a+b+c}")
print()
#5---------------
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^ ")
print()
#4----------------
from math import *
from re import *
print("keskmine")
a=float(input("1 number =>"))
b=float(input("2 number =>"))
v=float(input("3 number =>"))
h=float(input("4 number =>"))
d=float(input("5 number =>"))
m=(a+b+v+h+d)/5
print(f"keskmine on {m}")
#3-----------------
print("Harjutus")
aeg = float(input("Mitu tundi kulus sõidub ? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print()
print("sinu kirus oli " + str(round(kiirus,2)) + " km/h")
#2-----------------
from math import *
print("Ristkülikukujulise maatküki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")
#1-----------------
from math import *
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
r=C/(2*pi)
print()
print("Puu radius", round(r,2))
d=2*r
print("Puu diagonal", round(d,2))
print(f"Vastus:/nPuu läbimõõduga {C} ümbermõõt võrdub {d}")
