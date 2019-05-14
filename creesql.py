import sqlite3
import random
fichierbdd=sqlite3.connect('table.db')
bdd=fichierbdd.cursor()
bdd.execute('''CREATE TABLE fleurs (taille real, couleur text,x real,y real,id real)''')
tableauFleur=[]
tableauCouleur=['blue','red','green','pink','purple','black','white','gray']
for i in range(1,800):
	tableauFleur.append((i,tableauCouleur[random.randint(0,len(tableauCouleur)-1)],i+2,i,i))
		
bdd.executemany('INSERT INTO fleurs VALUES (?,?,?,?,?)',tableauFleur)
for row in bdd.execute('SELECT * FROM fleurs'):
	print(row)
fichierbdd.commit()
fichierbdd.close()
