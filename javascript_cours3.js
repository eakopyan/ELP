/** Principe du callback : le mécanisme de callback est une solution pour ne pas bloquer une exécution monothreadée. 
Très utilisé dans les systèmes asynchrones (l'exécution des fonctions n'est pas bloquante : l'ordre d'exécution peut 
changer selon la rapidité du réseau, le trafic de données, etc.)
Approche fonctionnelle (par opposition à l'impérative) : pas de retour au programme de base ( = indentations de programmes). 
Les fonctions servent de "points de rupture" dans le scheduler JavaScript (exécution des programmes). Toute méthode impérative 
possède un équivalent en fonctionnel.
File événementielle : file d'attente d'exécution de fonctions. Une fonction ajoutée à la file se retrouve forcément à la
fin et sera donc exécutée en dernier.
*/

// Fonction synchrone
function test() {
  for (let i = 0; i < 20; i++) {
    console.log("coucou", i);
  }
  return "Terminé";
}
result = test();      // output : Coucou 0... Coucou 19
console.log("->", result);    // output : Terminé

// Approche fonctionnelle (pas de return)
function test(f) {    //prend en paramètre une fonction invoquée à la fin
  for (var i = 0; i < 20; i++) {
    console.log("coucou", i);
  }
  f("Terminé");       // on ne revient pas au programme de base !
}
test(function(message) {        // output : Coucou 0...19   -> Terminé
  console.log("->", message);
});

// La même fonction, asynchrone
function test(f) {
  setTimeout(function () {      //place la fonction dans la file événementielle
    for (var i = 0; i < 20; i++) {
      console.log("coucou", i);
    }
    f();
  })
}
console.log("Debut");     // affiché en premier
test(function() {  // on place function(){ for...} à la fin de la file
  console.log("-> Terminé"); 
});
console.log("Fin")        // affiché en deuxième, AVANT l'affichage de la fonction test() !

// Pour avoir une boucle infinie fonctionnelle (le while() est impératif !!)
function f() {
  console.log("Debut");    
  test(function() {  
    console.log("-> Terminé"); 
  });
  console.log("Fin") 
  setTimeout(f())     // rajoute l'appel récursif en fin de liste
}
f()

//----------------------------------------------------------
/** Lire le contenu d'un fichier :fs.readFile() (charger la fonction à l'aide d'un require('fs'))
* signature : fs.readFile(<string/buffer/URL/int> path [<object/string> options], <function> callback)
* <error> err
* <string/buffer> data
*/
fs.readFile('/etc/passwd', (err, data) => {
  if (err) throw err;
  console.log(data);
});

//---------------------------------------------------------
/** Faire un GET sur une page WEB : http.request() (charger la fonction à l'aide d'un require('http'))
* signature : http.request(<object/string/URL> options, <function> callback)
*/

const options = {
  hostname: 'www.google.com',
  port: 80,
  path: '/upload',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': Buffer.byteLength(postData)
  }
};

const req = http.request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`);
  console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
  res.setEncoding('utf8');
  res.on('data', (chunk) => {
    console.log(`BODY: ${chunk}`);
  });
  res.on('end', () => {
    console.log('No more data in response.');
  });
});

req.on('error', (e) => {
  console.error(`problem with request: ${e.message}`);
});

