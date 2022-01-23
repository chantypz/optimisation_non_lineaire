# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:08:07 2022

@author: chant
"""


def f(x):
	return x**5 - 5*x**3 - 20*x + 5

def fprime(x):
	return 5*x**4 -15*x**2 -20

def fseconde(x):
	return 20*x**3 -30*x


def PasFixe(p):
	i=1
	x=0
	print('Etape 0')	
	print("x + i*p = ",x,"|			f'(0) = ",f(x))
	print('\n')	

	while f(x+i*p)<f(x+(i-1)*p):
		i+=1
		print("x + i*p = ",float(round(x+i*p,2)),"|			f(x+i*p) = ",float(round(f(float(round(x+i*p,2))),2)), "|		f(xi) > f(x(i-1)) ? ",f(float(round(x+i*p,2)))>f(float(round(x+(i-1)*p)))) 
		# Attention float(round()) sert à tronquer la valeur de x, donc à adapter par rapport au pas


	i+=1
	print("x + i*p = ",float(round(x+i*p,2)),"|			f(x+i*p) = ",float(round(f(float(round(x+i*p,2))),2)), "|			f(xi) > f(x(i-1)) ? ",f(x+i*p)>f(x+(i-1)*p))	







def PasAccelere(p):
	i=1
	x=0
	pdebut=p
	print('Etape 0')	
	print("x + i*p = ",x,"|			f'(0) = ",f(x))
	print('\n')	

	while f(x+i*p)<f(x+(i-1)*p):
		i+=1
		print('Pas : ',p,' | ',"		x + i*p = ",float(round(x+i*p,2)),"|			f(x+i*p) = ",float(round(f(float(round(x+i*p,2))),2)), "|		f(xi) > f(x(i-1)) ? ",f(float(round(x+i*p,2)))>f(float(round(x+(i-1)*p)))) 
		p=2*p


	i+=1
	print('Pas : ',p,' | ',"			x + i*p = ",float(round(x+i*p,2)),"|			f(x+i*p) = ",float(round(f(float(round(x+i*p,2))),2)), "|			f(xi) > f(x(i-1)) ? ",f(x+i*p)>f(x+(i-1)*p))

	i=i-2 # Le point précédent étant plus proche de l'optimum on choisit de revenir 2 points en arrière et de recommencer le processus

	print('\n')
	print('Repartons en arrière et reprenons un pas plus petit')
	print('\n')

	p=pdebut
	while f(x+i*p)<f(x+(i-1)*p):
		i+=1
		print('Pas : ',p,' | ',"		x + i*p = ",float(round(x+i*p,2)),"|			f(x+i*p) = ",float(round(f(float(round(x+i*p,2))),2)), "|		f(xi) > f(x(i-1)) ? ",f(float(round(x+i*p,2)))>f(float(round(x+(i-1)*p)))) 
		p=p




def Bissection(a,b,e):


    while abs(a-b)>e:
    	x=(a+b)/2
    	print(x)
    	if fprime(a)*fprime(x)<0:
    		b=x
    	else:
    		a=x
    	



#PasFixe(0.05)
#PasAccelere(0.05)
Bissection(0,2.5,0.05)