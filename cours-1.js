let a = function(a,b){
  return a+b
}
console.log(a(4,5))



let mult1 = function(a,b){
  return a*b
}
console.log("Result mult1(2,8) = " + mult1(2,8))

function multiplieur(a){
  return function (b) {
    return mult1(a,b)
  }
}
x = multiplieur(2)
console.log("Result multiplieur = "+x(8))


// Les deux fonctions suivantes renvoient la même chose !

function create(){
  let reponse = 23
  return function (x) {
    return x + reponse
  }
}

let a = create()
console.log(a(12))

function create(){
  this.reponse = 23
  this.calc = function (x) {
    return x + this.reponse
  }
}
let a = new create()
console.log(a.calc(12))


//Nombre d'arguments et principe de curryfication
function moins(a,b,c) {
  return (a-b)
}
console.log("moins(3,2) = "+moins(3,2))           //affiche 1
console.log("moins(3,2,4,8) = "+moins(3,2,4,8))   //affiche 1
console.log("moins(2) = "+moins(2))               //affiche NaN


valeurs = [0,2,4,6,8,10]

for(i=0; i<valeurs.length; i++){
  console.log(valeurs[i])
}
