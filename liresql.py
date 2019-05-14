import sqlite3
fichierbdd=sqlite3.connect('table.db')
bdd=fichierbdd.cursor()
for row in bdd.execute('SELECT * FROM fleurs;'):
		print('je suis la fleur n°{0} je suis {1} et je fait {2}'.format(row[4],row[1],row[0]))
		
