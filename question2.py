# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:10:05 2022

@author: chant
"""


def f(x):
	return x**3 -7*x**2 +8*x -3

def fprime(x):
	return 3*x**2 -14*x +8

def fseconde(x):
	return 6*x -14

def NewtonRaphson(x,e):
	print('\n')
	i=0
	print('Etape ',i,'\n x = ',x, '\n f(x) = ', f(x))

	x=x-f(x)/fprime(x)
	i=i+1
	print('\n')

	print('Etape ',i,'\n x = ',x, '\n f(x) = ', f(x))
	print('\n')



	while (abs(f(x))>e):
		i+=1
	
		
		x=x-f(x)/fprime(x)
		print('Etape ',i,'\n x = ',x, '\n f(x) = ', f(x))
		print('\n')	

#NewtonRaphson(5,0.001)


def NewtonRaphsonPrime(x,e):
	print('\n')
	i=0
	print('Etape ',i,'\n x = ',x, "\n f'(x) = ", fprime(x))

	x=x-fprime(x)/fseconde(x)
	i=i+1
	print('\n')

	print('Etape ',i,'\n x = ',x, "\n f'(x) = ", fprime(x))
	print('\n')



	while (abs(fprime(x))>e):
		i+=1
	
		
		x=x-fprime(x)/fseconde(x)
		print('Etape ',i,'\n x = ',x, "\n f'(x) = ", fprime(x))
		print('\n')	


NewtonRaphsonPrime(5,0.001)