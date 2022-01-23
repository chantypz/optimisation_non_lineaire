# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 01:03:49 2022

@author: chant
"""


import sys
from PyQt5 import QtWidgets

import numpy as np

from scipy.misc import derivative


class interface1(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.k5=0
		self.k4=0
		self.k3=0
		self.k2=0
		self.k1=0
		self.k0=0

		self.ki=0
		self.ka=0


		self.init_ui()


	def init_ui(self):

		# 
		self.x5=QtWidgets.QLabel('Coefficient x^5')
		self.l5 =QtWidgets.QLineEdit()

		# 
		self.x4=QtWidgets.QLabel('Coefficient x^4')
		self.l4 =QtWidgets.QLineEdit()

		# 
		self.x3=QtWidgets.QLabel('Coefficient x^3')
		self.l3 =QtWidgets.QLineEdit()

		# 
		self.x2=QtWidgets.QLabel('Coefficient x^2')
		self.l2 =QtWidgets.QLineEdit()

		# 
		self.x1=QtWidgets.QLabel('Coefficient x^1')
		self.l1 =QtWidgets.QLineEdit()

		# 
		self.x0=QtWidgets.QLabel('Coefficient x^0')
		self.l0 =QtWidgets.QLineEdit()

		self.xi=QtWidgets.QLabel('Point initiale')
		self.li =QtWidgets.QLineEdit()

		self.xa=QtWidgets.QLabel('Epsilon')
		self.la =QtWidgets.QLineEdit()

		# Bouton calcul
		self.b = QtWidgets.QPushButton('Suivant')
		self.b.clicked.connect(self.btn_suivant_clk)

		#Layout
		v_box = QtWidgets.QVBoxLayout()

		v_box.addWidget(self.x5)
		v_box.addWidget(self.l5)

		v_box.addWidget(self.x4)
		v_box.addWidget(self.l4)

		v_box.addWidget(self.x3)
		v_box.addWidget(self.l3)

		v_box.addWidget(self.x2)
		v_box.addWidget(self.l2)

		v_box.addWidget(self.x1)
		v_box.addWidget(self.l1)

		v_box.addWidget(self.x0)
		v_box.addWidget(self.l0)

		v_box.addWidget(self.xi)
		v_box.addWidget(self.li)

		v_box.addWidget(self.xa)
		v_box.addWidget(self.la)

		v_box.addWidget(self.b)

		self.setLayout(v_box)

		#Fenetre
		self.setWindowTitle('Interface')
		self.show()


	def btn_suivant_clk(self):

		print('\n')		

		self.k5= int(self.l5.text())
		#print('Coefficient x^5 : ',self.k5)
		self.k4= int(self.l4.text())
		#print('Coefficient x^4 : ',self.k4)
		self.k3= int(self.l3.text())
		#print('Coefficient x^3 : ',self.k3)
		self.k2= int(self.l2.text())
		#print('Coefficient x^2 : ',self.k2)
		self.k1= int(self.l1.text())
		#print('Coefficient x^1 : ',self.k1)
		self.k0= int(self.l0.text())
		#print('Coefficient x^0 : ',self.k0)


		print('Le polynome de la fonction : ', self.k5,'* x**5 + ',self.k4,'* x**4 + ',self.k3,'* x**3 + ',self.k2,'* x**2 + ',self.k1,'*x**1 + x',self.k0)

		self.ki= int(self.li.text())
		print('Point initiale : ',self.ki)

		self.ka= float(self.la.text())
		print('Epsilon : ',self.ka)

		print('\n')


		print(self.NewtonRaphson())

	# Partie Fonction NewtonRaphson
	def Fonction(self,x):
		f= self.k5*x**5+self.k4*x**4+self.k3*x**3+self.k2*x**2+self.k1*(x**1) + self.k0
		return f

	def Derivee(self,x):
		return derivative(self.Fonction,x)

	def Seconde(self,x):
		return derivative(self.Derivee,x)

	def NewtonRaphson(self):
		i=0
		
		x=self.ki  #Point initiale

		f=self.Fonction(x)
		fprime=self.Derivee(x)
		fseconde=self.Seconde(x)


		while (abs(fprime)>self.ka): #ka =epsilon
			print('Etape ',i,' : x = ', x)
			i+=1
			print('f(x) = ',f)
			print("f'(x) = ",self.Derivee(x))
			print("f''(x) = ",self.Seconde(x)," | Fin d'etape")
			x=x- fprime/fseconde
			f=self.Fonction(x)
			fprime=self.Derivee(x)
			fseconde=self.Seconde(x)
			print('\n')
		return x
			




app = QtWidgets.QApplication(sys.argv)
a_window = interface1()
sys.exit(app.exec_())