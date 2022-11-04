"""Da se napravi programa vo koja korisnikot ke vnese 
2 broevi i da se proveri dali zbirot e pomal od 100"""
print('                                                    ')
print('IGRA')
print('__________________________________________________________________')
print('Proverka dali zbirot na dva broja e pomal od 100')
print('__________________________________________________________________')
x=int(input('vnesi broj x '))
y=int(input('vnesi broj y '))
z=x+y
if z<100:
    print('zbirot na {} i {} iznesuva {} i e pomal od 100'.format(x,y,z))
elif z>100:
    print('zbirot na {} i {} iznesuva {} i e pogolem od 100'.format(x,y,z))
else:
    print('zbirot na {} i {} iznesuva {}'.format(x,y,z))
print('_______________________________________________')

"""Da se napravi programa vo koja korisnikot ke vnese godina na 
ragjanje, ke se presmeta kolku godini e i da se odredi dali e maloleten ili polnoleten"""


x=int(input('vnesi godina na ragjanje '))
y=2022-x 

if y>=18 and y<110 and y>=0:
    print('korisnikot ima {} godini, i e polnoleten.'.format(y))

elif y<18 and y<110 and y>=40:
    print('korisnikot ima {} godini, i e maloleten.'.format(y))
else:
    print('vnesovte nerealen podatok.')
print('__________________________________________________________________')

"""Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici, 
da se presmeta plostinata i da se proveri koj pravoagolnik e pogolem"""
print('Da se sporedat plostinite na 2 pravoagolnici:')
print('__________________________________________________________________')
print('Vnesete podatoci za pravoagolnik 1 so strani x i y:')
x=int(input('vnesi strana x na pravoagolnik '))
y=int(input('vnesi strana y na pravoagolnik '))
z=x*y
print('plostinata na pravoagolnik 1 so strani {} i {} e {}'.format(x,y,z))
print('__________________________________________________________________')
print('Vnesete podatoci za pravoagolnik 2 so strani c i d:')
c=int(input('vnesi strana c na pravoagolnik '))
d=int(input('vnesi strana d na pravoagolnik '))
g=c*d
print('plostinata na pravoagolnik so strani {} i {} e {}.'.format(x,d,g))

print('__________________________________________________________________')
if z>g:
    print('plostinata na pravoagolnik 1 e pogolema od plostinata na pravoagolnik 2.')
elif z<g:
    print('plostinata na pravoagolnik 1 e pomala od plostinata na pravoagolnik 2.')
else:
    print('plostinite se ednakvi.')
print('_________________________________________________________________')

"""Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite na
 triagolnici, i da se proveri dali so tie golemini moze da se kreira 
 triagolnik(zbirot treba da bide 180)"""

print('Dali so vnesenite agli moze da se kreira triagolnik?:')
print('__________________________________________________________________')
a=int(input('vnesi agol a '))
b=int(input('vnesi agol b '))
c=int(input('vnesi agol c '))
zbir=a+b+c
if zbir==180:
    print('DA, moze da se kreira triagolnik')
else:
    print('NE moze da se kreira triagolnik')
print('______________________________________________________________')

"""Da se napravi programa vo koja korisnikot ke vnese nekoe ime i da se proveri 
sekoga samoglaska kolku pati se pojavuva vo ime i od kolku karakteri e sostaveno toa ime"""

ime=input('Vnesi ime ')
x=len(ime)
a = ime.count("a")
e = ime.count("e")
i = ime.count("i")
o = ime.count("o")
u = ime.count("u")
print('Imeto ima {} bukvi. ' .format(x))
print('Imeto ima gi ima slednive samoglaski: a - {} pati, e - {} pati, i - {} pati, o - {} pati, u - {} pati.'.format(a,e,i,o,u))
print('______________________________________________________')
