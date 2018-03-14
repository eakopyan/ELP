/** 
Le multithread étend l'idée du multitâche aux applications, de sorte que vous pouvez sous-diviser des opérations spécifiques au 
sein d'une même application en threads individuels. Chaque thread peut fonctionner en parallèle. Le système d'exploitation divise 
le temps de traitement non seulement entre différentes applications, mais aussi entre chaque thread dans une même application.
Promesses : objet représentant l'accomplissement ou l'échec d'une opération asynchrone, peut produire une valeur unique dans le futur. Une promesse doit être dans l'un des 3 états : accomplie,
rejetée, en attente. Elle est lancée dès sa création.

Plus d'infos sur https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Utiliser_les_promesses

*/

Promise = require('bluebird');

// modèle de déclaration d'une promesse
wait = function(time) {  // wait est une promesse
  a = new Promise(function(resolve) { // resolve = fonction, paramètre de la promesse
    setTimeout(resolve, time);
  });
  return a;
}

// modèle d'utilisation d'une promesse
// then = mot-clé associé aux promesses, permet de déclencher la suite si promesse résolue
wait(3000).then(function() { console.log('Bonjour');})  // ce qui est placé avant le then renvoie une promesse


// Traiter le rejet d'une promesse :
  a = new Promise(function(resolve, reject) {
    if (time>3000) {
      reject('erreur')
    } else {
      setTimeout(resolve, time)
  })};
  return a;

// Test des deux cas possibles : succès ou échec
// catch = mot-clé associé aux promesses, permet de gérer la suite dans le cas d'un rejet de promesse
wait(2000)  // le then va s'exécuter
.then(
    function(res) { 
      console.log('Cool', res) 
      return wait(4000)
    }
)
.catch(
  function(res) { console.log('Erreur', res) }
)
// Affichage : Cool \n Erreur
