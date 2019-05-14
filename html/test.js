new Vue({//declarer vuejs
  el: '#app',//element qui a l'id app
  data: {//mes variables
    users: []//variable qui contiendra la reponce de la requete
  },//fermeture de data
  created() {//fonction created
    var vm =axios//importe axios
      .get('http://localhost:5000/toto') //requete get sur l'url indiquer
      .then(function(response) {//fonction pour la reponce de la requete
        vm.users = response.data// ajout de la reponce a la variable users
      })//fermeture axios
  }//fermeture de la fonction created
})//fermeture de vuejs
