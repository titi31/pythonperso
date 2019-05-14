import os#importe module os
from flask import Flask, render_template, Markup,json,request,make_response,jsonify # importe flask pour le template, render_template pour affiche template et markup pour executer du code html et css dans le template
import sqlite3
template_dir = os.path.abspath('templates')#indique le chemin du template
app = Flask(__name__,template_folder=template_dir)#pour lancer flask
file=[]#liste vide qui contiendra les fichier txt
image=[]#liste vide qui contiendra les image jpeg
mesfichier=[]#liste vide qui contiendra les images et les fichiers
for i in os.listdir('static/document'):	#boucle qui tous les fichiers qui se situe dans static/document
	if i.endswith('.txt'):#verifie si l'extension est en txt
		fichier=open('static/document/{}'.format(i),'r')#ouvre les txt en lecture seulement
		file.append(Markup("<div style=\"border: 2px red solid; \"><p>"+fichier.read()+"</p></div>"))#ajoute txt a file en mettant les fichiers dans un div
		fichier.close()
		fichier1="".join(file)#convertit file chaine de caractere
	elif i.endswith('.jpeg'):# verifie si l'extension est en jpeg
		image.append(Markup("<div style=\"border: 2px yellow solid;\"><img src=static/document/"+i+"></div><br>"))#ajoute a image les jepg dans un div 
		img="".join(image)	#convertit image en chaine de caractere pour pouvoir l'ajouter apres au template
@app.route('/')#lance le serveur a l'url localhost:5000
def html():#fonction qui indique ce que fait le serveur
	
	mesfichier.append(fichier1)#ajoute fichier(txt) a mesfichier
	mesfichier.append(img)#ajoute img a mesfichier
	mesfile="".join(mesfichier)#convertit mesfichier en chaine de caractere pour l'ajouter dans le template
	if len(mesfile)<310:
		return render_template('front.html',message=mesfile)#affiche le template avec dans la variable message tout ce que contient mesfile
	else:
		file[:]=[]#liste vide qui contiendra les fichier txt
		image[:]=[]#liste vide qui contiendra les image jpeg
		mesfichier[:]=[]
		return render_template('front.html',message=mesfile)
@app.route('/route', methods=['POST','GET'])#lance le serveur a l'url localhost:5000/route
def route():#fonction qui decrit ce que fait le serveur
	return render_template('front.html')#affiche le template
@app.route('/c')#lance le serveur a l'url localhost:5000/c
def nb_cookie():#fonction qui decrit ce que fait le serveur
	cookie=[]#liste vide pour inserer les cookies
	for i in range(len(request.cookies)):#boucle for pour connaitre le nombre de cookies
		if "cookie{}".format(i) in request.cookies:#verifie le nombre de cookies
			cookie.append(request.cookies.get('cookie{}'.format(i)))#ajoute les cookies a la liste cookie
	cookie1=" ".join(cookie)#convertit la liste en chaine de caractère pour afficher les cookies ensuite
	return "vous avez {} cookies et leur valeur sont: ".format(len(cookie))+cookie1#affiche le nombre de cookies et leurs valeurs
@app.route('/cookie', methods=['POST'])#lance le serveur a l'url localhost:5000/cookie
def get_cookie():#fonction qui dit ce que fait le serveur
	user=json.loads(request.data)#convertit la reponce en json
	print(user)#affiche la reponce
	resp=make_response(render_template('front.html'))#crée pour reponce le template
	if user=={'data':{'a':True,'b':False}}:#verifie si A est coché 
		cookie=resp.set_cookie('a','a is true')#crée un cookie
		name=request.cookies.get('a')#envoie le cookie a l'utilisateur 
		print(name)#affiche le cookie dans le serveur sert de test pour le developpeur
	if user=={'data':{'a':False,'b':True}}:#verifie si B est coché
		cookie=resp.set_cookie('b','b is true')#crée un cookie
		name=request.cookies.get('b')#envoie le cookie a l'utilisateur
		print(name)#affiche le cookie dans le serveur sert de test pour le developpeur
	if user=={'data':{'a':True,'b':True}}:#verifie si les 2 checkbox sont coché
		cookie=resp.set_cookie('a','a is true')#cree un cookie pour a
		name=request.cookies.get('a')#envoie le cookie A a l'utilisateur
		cookie1=resp.set_cookie('b','b is true')#cree un cookie pour b
		name1=request.cookies.get('b')# envoie le cookie b a l'utilisateur
		print(name)#affiche le cookie A sur le serveur test pour developpeur
		print(name1)#affiche le cookie b sur le serveur test pour developpeur
	for valu in user.values():#boucle for pour connaitre le chiffre rentrer par l'utilisateur
		print(valu)#affiche le nombre test pour developpeur
		for nb in range(valu):#compte jusqu'au nombre choisit
			print(nb)#affiche nombre test pour developpeur
			resp.set_cookie('cookie{}'.format(nb),'text{}'.format(nb))#cree le nombre de cookie correspondant au nombre 
			request.cookies.get('cookie{}'.format(nb))#envoie les cookies a l'utilisateur
	return resp#affiche le template
class ordinateur(object):#cree un object ordinateur
	def __init__(self):#fonction ou il y a les instance de l'objet
		self.nom='tinou'#instance
		self.ip='85.56.02.12'#instance
		self.browser='tor'#instance
		self.engine_search='yacy surtout pas google'#instance
		self.social_network='mastodonte surtout pas facebook'#instance
pc=ordinateur()#fixe l'object dans une variable
@app.route('/toto', methods=['GET','POST'])#lance le serveur a l'url localhost:5000/toto en get ou post
def obj():#indique ce que fait le serveur
	ordi=pc.__dict__#convertit l'object en dictionnaire
	json_obj = jsonify(ordi)#convertit le dictionnaire en json
	json_obj.headers.add('Access-Control-Allow-Origin', '*')#autorise les requete sur le serveur
	return json_obj#affiche le json
from jinja2 import Environment, FileSystemLoader, meta#import jinja2,environement pour lire le template,filesystemloader pour lire le template
#et meta pour lire le template parser
def page(file):#fonction qui sert a reutiliser le programme pour n'importe quel template
	env = Environment(loader=FileSystemLoader('templates'))#indique le dossier du template
	template_source = env.loader.get_source(env,file)#lit le template
	parsed_content = env.parse(template_source)#parse le template
	dic=meta.find_undeclared_variables(parsed_content)#lit le template parser
	return (dict.fromkeys(dic,''))#transforme les variable du template mis en ensemble en dictionnaire
f=page('front.html')#utilise la fonction pour le template test.html
print(f)#affiche la fonction
@app.route('/connection')#lance le serveur avec l'url localhost:5000/connection
def connecter():#fonction pour indiquer ce que fait le serveur
	return render_template('front.html')#affiche mon template
@app.route('/login', methods=['POST'])#lance serveur avec l'url localhost:5000/login et en requete post
def login():#fonction pour dire ce que fait le serveur
	user=json.loads(request.data)#voir la reponce sous forme de json
	print(user)#affiche la reponce
	resp=make_response(render_template('front.html'))#fixe le template en reponce dans une variable
	if user=={'data':{'login':'admin','password':'azerty'}}:#verifie que le login et le password est correct
		resp.set_cookie('correct','ok')#cree un cookie
		request.cookies.get('correct')#envoie le cookie a l'utilisateur
	return resp #retourne la reponce
@app.route('/json',methods=['GET'])#lance le serveur  a l'url localhsot:5000/json en requete get
def get():#fonction qui indique ce que fait le serveur
	with open("data2.json","r") as json_data:#ouvre le fichier en lecture seulement
		fileJson= json.load(json_data)#convertit le fichier en json
	if 'correct' in request.cookies:#verifie si il y a le cookie
		return jsonify(fileJson)#affiche le fichier json
	else:#action faite si il n'y a pas de cookie
		abort(401)#le serveur doit repondre 401 (erreur 401 pour dire qu'il n'est pas connecter)
@app.route('/change',methods=['POST'])#lance serveur a l'url localhost:500/change en requete post
def change():#fonction qui indique ce que fait le serveur
	print(json.loads(request.data)) #affiche la reponse de la requete en json 
	#fichier.write(js)
	#fichier.close()
	return render_template('front.html')# affiche le template
@app.route('/jardin')
def monjardin():
	fichierbdd=sqlite3.connect('table.db')
	bdd=fichierbdd.cursor()
	jardin=[]
	for row in bdd.execute('SELECT * FROM fleurs'):
		jardin.append(row)
	return jsonify(jardin)
if __name__ == '__main__':#verifie l'url taper
	app.run(debug=True)	#execute le site avec le mode debogage activer
	


