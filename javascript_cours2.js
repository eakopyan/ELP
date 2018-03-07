/** Langage orienté objet :
1) Abstraction par des classes (initialisation)
2) Les classes communiquent entre elles par messages
3) Les variables internes aux objets ne sortent pas (protection par encapsulation) : this permet d'y accéder.
En JavaScript, tout est objet : opérateur typeof() ou on peut appliquer une fonction à n'importe quel type de 
variable (notion d'héritage).
Langage de niveau supérieur : Coffeescript (terminal en ligne sur www.coffeescript.org > Try Coffeescript
*/

// Création d'une classe simple
class Machine {
    constructor(){
        this.utilite = "rien"
    }
}

let machine = new Machine()     // machine : [object Object]: {utilite: "rien"}

function create(){ this. reponse = 23 }
create.prototype.calc = function(x) { return x + this.reponse }     // définition d'une fonction dans une classe (prototype)
function create2(){ this.reponse = 32 }
create2.prototype = new create()        // principe d'héritage, output : [object Object]: {reponse: 23}
create2.prototype.hello = function() { console.log("hello!")}

//-------------------------------------------------------------------
// Fonctions bind(), call() et apply() : fonctions de bas niveau = fonctions d'assemblage pour des langages de plus haut niveau
function parle(){ console.log(this.me, "dit quelque chose.")}
parle()         // output : undefined dit quelque chose.

function phrase(s) {console.log("Vous dites : " + s)}
phrase.call(null, "Bonjour")    // ou .apply(null, ["Bonjour"]), null correspond au contexte (pas de this dans la fonction)
