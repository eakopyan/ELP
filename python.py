# -*- coding: utf-8 -*-
"""Doc officielle de Python : https://docs.python.org/3/ et python package index
Bien regarder les références & tutos pour réviser
Bouts de codes sur python cookbook
"""

""" exécuter un fichier dans terminal python : %run <nomProg>
 exécuter un fichier dans invite de commande : python3 <nomProg>
 sauvegarder les commandes du terminal : %save """

"""TUPLES : t = (1,2) ; t= 1, ; t=() IMMUABLE !!"""
IN [26]: a
Out[26]: 2

In [27]: b
Out[27]: 5

In [28]: a,b = b,a

In [29]: a
Out[29]: 5

In [30]: b
Out[30]: 2

fruits=["oranges", "kiwis", "apples"]

for i, f in enumerate(fruits):
    print(i,f)

0 oranges
1 kiwis
2 apples

"""DICTIONNAIRES : d={}       MUABLE"""
d = {"raz":1982, "eak":1997, "guido":1955, "katu":2013}

d
Out[37]: {'eak': 1997, 'guido': 1955, 'katu': 2013, 'raz': 1982}

for k in d:
    print(k)

eak
guido
katu
raz

for k in d.items():
    print(k)

('eak', 1997)
('guido', 1955)
('katu', 2013)
('raz', 1982)

Initialisation à partir d'une liste de tuples
d = [("r", 1982),("e",1997)]

type(d)
Out[40]: list

dd = dict(d)

dd
Out[42]: {'e': 1997, 'r': 1982}


"""Entrées - sorties de fichiers :"""
f = open("/home/eakopyan/Bureau/species-intro.txt")

for line in f:
    print(line)

When on board H.M.S. Beagle, as naturalist, I was much struck with

certain facts in the distribution of the organic beings inhabiting South
......

 f.close()

#exo 1 : compter le nombre d'instances de chaque mot dans le texte
#utiliser un dictionnaire ("mot":nbApparitions)
#dir(variable) : donne la liste des fonctions applicables au type de la variable

with open("/home/eakopyan/Bureau/species-intro.txt") as f:      //forme : with (constructeur) as (variable):
    histogram = {}
    for line in f:
        words = [w.lower() for w in line.split()]   // harmoniser la caste des mots (tout en minuscules)
        for word in words:
            for c in "{}[]-_.;:',!?\/":              // block nettoyage de ponctuation
                if c in word:
                    word = word.replace(c, "")
            if word not in histogram:
                histogram[word] = 1
            else:
                histogram[word] += 1
    pass

#Joli affichage :
for k in sorted(list(histogram.keys())):
    print("{0:18} | {1}".format(k, histogram[k] * "*"))     // technique de formatage


"""DEFINITION DE FONCTIONS : def <nomFonction>(<arguments>): <contenu> """
def f(a, v, u):
    a = 3
    v.append(4)
    u = [666,777]


f(x, vv, uu)

x
Out[71]: 6     #reste inchangé !

vv
Out[72]: [1, 2, 4]

uu
Out[73]: [3, 4]     #reste inchangé !


#Valeurs par défaut :
def f(a=3, b=0):
    return a+b


f()
Out[77]: 3

f(1,5)
Out[78]: 6

#On peut spécifier les arguments par mot-clés :
f(7)
Out[80]: 7

f(b=7)
Out[81]: 10


"""ARGUMENTS OPTIONNELS : *args"""
def f(name, *args, **kwargs):
    print(name)
    print(args)
    for k in kwargs:
        print(k, kwargs[k])

f("eak")
eak
()

f("eak", 1,2)
eak
(1, 2)      //il s'agit d'un tuple !

f("ako", 1, None, age=21, job="student")
ako
(1, None)
job student
age 21


def f(*args, sep="/"):
    return sep.join(args)


f("usr", "local", "host")       OU      f(*["usr", "local", "host"]) //extracteur, valable que dans les appels fct
Out[87]: 'usr/local/host'


#exo 2 : manipulation de dictionnaire et mise en mémoire
def f(a, b, _cache={}):
   if (a,b) in _cache:
        print("Already in cache")
        return _cache[(a,b)]
   else:
       print("Computing...")
       result = a**b
       _cache[(a,b)] = result
       return result


def f(n):
    def g(x):
        return x+n
    return g

#Equivalent à la fonction anonyme :

def f(n):
    return lambda x: x+n

#Autre usage :
words
Out[128]: ['Mary', 'had', 'a', 'little', 'lamb']

In [129]: sorted(words)
Out[129]: ['Mary', 'a', 'had', 'lamb', 'little']

In [130]: sorted(words, key=lambda w:w.lower())
Out[130]: ['a', 'had', 'lamb', 'little', 'Mary']


sorted(d)
Out[132]: ['eak', 'guido', 'katu', 'raz']

In [133]: sorted(d.items(), key = lambda t: t[1])
Out[133]: [('guido', 1955), ('raz', 1982), ('eak', 1997), ('katu', 2013)]



"""MODULES : regarder www.python.org référence librairie standard
Python trouve les modules et packages grâce à sys.path (import sys)"""
import fibonacci

type (fibonacci)
Out[3]: module

dir(fibonacci)
Out[4]:
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'fib1',
 'fib2']

fibonacci.fib1(10)
Out[5]: [1, 1, 2, 3, 5, 8]

#OU
from fibonacci import fib1, fib2

fib1(10)

"""PACKAGES : collection logique de modules (dossier) (cf www.python.org)
Toujours avoir un fichier __init__.py, même s'il est vide !!!"""


"""CLASSES"""
class MyClass:
    myPi = 3.17

type(MyClass)
Out[29]: type

m = MyClass()

type(m)
Out[34]: __main__.MyClass

In [35]: MyClass.myPi
Out[35]: 3.17

In [36]: m.myPi
Out[36]: 3.17



class MyClass:
    myPi = 3.17
    def __init__(self, v):
        self.value = v
    def f():                    #Méthode statique ne recevant PAS de self !
        print("Hello world")
    def set(self, v):
        self.value = v
    def __repr__ (self):        #permet d'avoir un affichage potable
        return "value = " + str(self.value)


m = MyClass(42)

m
Out[44]: value = 42

print(m)
value = 42

MyClass.f()
Hello world


"""ESPACE DE NOMMAGE, PORTEE (NAMESPACE, SCOPE)
NAMESPACE = mapping entre identifiant et objet
SCOPE = zone textuelle de Python où un namespace est accessible directement
4 étages de scopes :
- local (fonction)
- non local (fonction mère / classe)
- global (module)
- built-ins (variables intégrées) """

def scope_test():
    def do_local():         #modification se fait uniquement au sein de do_local()
        name = "local name"
    def do_nonlocal():      #modification se fait dans la fonction englobante
        nonlocal  name      #nonlocal = mot-clé
        name = "nonlocal name"
    def do_global():        #modification se fait dans le module
        global name         #global = mot-clé
        name = "global name"
    name = "test name"
    do_local()
    print("After local assignment: ", name)
    do_nonlocal()
    print("After nonlocal assignment: ", name)
    do_global()
    print("After global assignment: ", name)


scope_test()
After local assignment:  test name
After nonlocal assignment:  nonlocal name
After global assignment:  nonlocal name

name
Out[78]: 'global name'


"""EXCEPTIONS = ERREURS (objets)
Type d'erreur : SyntaxError, IndexError, ZeroDivisionError...
3 étapes :
- action où on anticipe une erreur -> try
- gestion de(s) l'erreur(s) -> except
- action où on n'anticipe pas d'erreur -> else
- clause finale, toujours exécutée même si on sort de la fonction -> finally"""

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("Result = ", result)
    finally:
        print("Executing finally clause.")


divide(8,2)
Result =  4.0
Executing finally clause.

divide(8,0)
Division by zero!
Executing finally clause.

#Exemple d'erreur inattendue :
divide("2", "5")
Executing finally clause.
Traceback (most recent call last): [... TypeError...]

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by zero!")
    except TypeError:
        print("Type error!")
    else:
        print("Result = ", result)
    finally:
        print("Executing finally clause.")


divide("2", "5")
Type error!
Executing finally clause.

#Pour gérer toutes les erreurs : ne pas spécifier l'erreur
except:
    print("Error!")

#Pour lever une erreur :
except Exception as e:
    print("Error!", e)
    raise   #on propage l'erreur = on ne fait rien avec l'objet plutôt que le propager



""" PROGRAMMATION ORIENTEE OBJET
!= Java: en Python, possible de dérivr de plusieurs classes
"""
class Shape:
    def __init__(self, x = 0, y = 0):   #initialisation
        self.x = x
        self.y = y
    def __repr__(self):         #représentation textuelle
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def translate(self, dx, dy):    #translation
        self.x += dx
        self.y += dy
    def area(self):         #méthodes vides pour le moment, complétées dans classes dérivées
        pass
    def perimeter(self):
        pass

s = Shape(9,6)

s
Out[3]: (9, 6)

class Circle(Shape):    #syntaxe d'héritage
    def __init__(self, x=0, y=0, r=0): #reprendre les attributs de la classe base
        super().__init__(x,y) #pas besoin du self à cause de la METHODE super() !!
        self.r = r
    def __repr__(self):
        return "(" + super().__repr__() + ": " + str(self.r) + ")"
    def area(self):
        return 3.14 * self.r **2
    def perimeter(self):
        return 2*3.14*self.r

c = Circle(r=6)

c.area()
Out[9]: 113.04

c.translate(2,4)

c
Out[13]: ((2, 4): 6)

issubclass(Circle, Shape)   #teste si une classe est la dérivée de la seconde
Out[14]: True

isinstance(c, Circle)   #teste si un objet est l'instance d'une classe
Out[15]: True

isinstance(c, Shape)    #un cercle est bien une instance de Shape !
Out[16]: True

class Rectangle(Shape):
    def __init__(self, x=0, y=0, l=0, w=0):
        super().__init__(x,y)
        self.l = l
        self.w = w
    def __repr__(self):
        return "["+ super().__repr__()+": "+str(self.l)+"x"+str(self.w)+"]"
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)


class Square(Rectangle):
    def __init__(self, x=0, y=0, s=0):
        super().__init__(x,y,s,s)

#Exercice : trier 10 shapes en fonction de leur aire
import random  #libraire pour l'aléatoire

In [47]: types = [Circle, Rectangle, Square] #les trois shapes dispo

In [49]: shapes = [] #pour l'instant, liste vide. Sera remplie ensuite

In [50]: for i in range(10):  #de 0 à 9
            idx = random.randrange(0,3)  #randrange génère un entier entre 0 et 2
            if types[idx] == Circle:
                shapes.append(Circle(r=random.randrange(0,10)))  #ajout de la shape au tableau
            elif types[idx] == Rectangle:
                shapes.append(Rectangle(l=random.randrange(0,10), w=random.randrange(0,10)))
            else:
                shapes.append(Square(s=random.randrange(0,10)))


shapes
Out[51]:
[((0, 0): 7),
 [(0, 0): 9x9],
 [(0, 0): 2x2],
 [(0, 0): 8x0],
 [(0, 0): 0x6],
 ((0, 0): 5),
 [(0, 0): 4x1],
 ((0, 0): 9),
 [(0, 0): 7x7],
 [(0, 0): 8x8]]

sorted(shapes, key = lambda t: t.area())  #shapes triées, dont la clé est une fonction lamda qui renvoie l'aire
Out[54]:
[[(0, 0): 8x0],
 [(0, 0): 0x6],
 [(0, 0): 2x2],
 [(0, 0): 4x1],
 [(0, 0): 7x7],
 [(0, 0): 8x8],
 ((0, 0): 5),
 [(0, 0): 9x9],
 ((0, 0): 7),
 ((0, 0): 9)]
 """area() est une méthode polymorphique : on peut l'utiliser sur plusieurs objets dérivés
 pour trier par ordre décroissant : sorted(shapes, key=..., reverse=True)

 HERITAGE SUR LES EXCEPTIONS
 """
 class A(Exception):
    pass

 class B(A):
    pass

try:
    raise B("B happened")
except A:
    print("A caught!")
except B:
    print("B caught!")

A caught! #B est un objet de type A: donc on affiche "A caught!". Maintenant si on inverse l'ordre...

try:
    raise B("B happened")
except B:
    print("B caught!")
except A:
    print("A caught!")

B caught!


""" ITERATEURS ET GENERATEURS

"""
class FibIter:  #itération sur la suite de Fibonacci
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.b <self.n:
            return self.b
        else:
            raise StopIteration()
    def __iter__(self):
        return self

class Reversed:  #protocole de base
    def __init__(self, seq):
        self.seq = seq
        self.pos = len(seq)
    def __next__(self):
        if self.pos > 0:
            self.pos -= 1
            return self.seq[self.pos]
        else:
            raise StopIteration()
    def __iter__(self):
        return self



def FibGen(n):
    a, b = 0, 1
    while b<n:
        yield b  #on récupère la valeur de b, et la fonction est bloquée jusqu'à appel d'un next
        a, b = b, a+b

f = FibGen(10)

In [81]: type(f)
Out[81]: generator

def reverse(seq):
    for i in range(len(seq)-1, -1, -1): #décrémentation jusqu'à 0 par pas de -1
        yield seq[i]

v = list(FibIter(15))

In [84]: v
Out[84]: [1, 2, 3, 5, 8, 13]

In [85]: for e in reverse(v):
    ...:     print(e)
    ...:
13
8
5
3
2
1
