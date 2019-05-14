import os #importe le module os 
from flask import Flask, render_template,request,json,make_response,jsonify,abort # importe flask pour faire des templates, render_templates pour afficher mes templates 
#request pour les reponces de mes requetes json pour transformer en json  make_response pour les reponse de mon serveur sans requete jsonify pour mettre le json en plus jolie 
# abort pour une reponse en erreur 400 
template_dir = os.path.abspath('templates')#indique ou se trouve mon template
app = Flask(__name__,template_folder=template_dir)#pour lancer flask
@app.route('/connection')#lance le serveur avec l'url localhost:5000/connection
def connecter():#fonction pour indiquer ce que fait le serveur
	return render_template('form.html')#affiche mon template
@app.route('/login', methods=['POST'])#lance serveur avec l'url localhost:5000/login et en requete post
def login():#fonction pour dire ce que fait le serveur
	user=json.loads(request.data)#voir la reponce sous forme de json
	print(user)#affiche la reponce
	resp=make_response(render_template('form.html'))#fixe le template en reponce dans une variable
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
	return render_template('form.html')# affiche le template
if __name__=="__main__":#verifie l'url
	app.run(debug=True)#lance le serveur en fonction de l'url indiquer avec le mode debogage activer
