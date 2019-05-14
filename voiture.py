from tkinter import *
fenetre=Tk()
import time
canvas=Canvas(fenetre,width=150,height=200,background="gray")
import random
class Voiture:
	def __init__(self,x,y,xx,yy,couleur):
		self.y=y
		self.x=x
		self.xx=xx
		self.yy=yy
		self.couleur=couleur
		self.rectangle=canvas.create_rectangle(self.xx,self.yy,self.x,self.y,fill=self.couleur)
		self.cercle=canvas.create_oval(50,50,70,70,fill="blue")
		
	#def run(self):
		
	#	while True:
liste=[]
couleur=["blue","red","black","pink","gray","yellow","white","purple","orange","green","maroon"]
x=0
y=10
xx=30
yy=25
listey=[]
toto=[]
#for i in range(100):
#	for color in couleur:
#		i=Voiture(x,y,xx,yy,color)
#		x=x+10
#		xx=xx+10
		#y=y+5
		#yy=y+5
#		i=Voiture(x,y,xx,yy,color)
#		if xx>=200:
#			x=0
#			xx=30
#			y=y+10
#			yy=yy+10
				
#canvas.pack()
#fenetre.mainloop()
for i in range(100):
	for color in couleur:
		i=Voiture(x,y,xx,yy,color)
		
		x=x+35
		xx=xx+35
		
		i=Voiture(x,y,xx,yy,color)
		if xx>=200:
			x=0
			xx=30
			y=y+15
			yy=yy+15
		liste.append(i)
while True:
	for i in liste:	
		
		i.x+=1
		i.xx+=1
		canvas.delete(i.rectangle)
		
		i.rectangle=canvas.create_rectangle(i.xx,i.yy,i.x,i.y,fill=i.couleur)
		if i.xx>=200:
			i.x=0
			i.xx=30
	canvas.pack()
	fenetre.update()
		
	


	
	

