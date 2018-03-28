-- fold : combine les valeurs d'une liste en partant de la droite (r) ou de la gauche (l)

foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f z [] = z
foldr f z (x:xs) = f x (foldr z f xs)
{- foldr f z [a,b,c] -> a 'f' (b 'f'(c 'f' z))
foldl f z [a,b,c] -> ((z 'f' a) 'f' b) 'f' c -}

-- Application de foldl à la fonction reverse
myReverse lst = foldl (\xs x -> x:xs) [] [1,2,3]
-- NB : (\xs x -> x:xs) = "lambda fonction qui prend xs et x et renvoie x concaténé à xs

-- Style point-free = sans argument (propriété d'application partielle)
myReverse = foldl (\xs x -> x:xs) []

-- Définition de fonctions avec foldr
import Prelude hiding (length, sum, product, and, or) -- on masque les fonctions que l'on souhaite redéfinir

-- length :: [a] -> Int
myLength = foldr (\_ x -> x+1) 0    -- pour foldl on aurait (\x _)

-- sum :: Num a => [a] -> a
mySum = foldr (+) 0

-- product :: Num a => [a] -> a
myProd = foldr (*) 1

-- and :: [Bool] -> Bool
myAnd = foldr (&&) True     -- idem pour foldl

-- or :: [Bool] -> Bool
myOr = foldr (||) False     -- idem pour foldl


---------------------------------------------------------------------------------------

-- Définition de types et de classes

-- Définition de types avec 'data' : data constructeurType [paramètres] = constructeurVal [paramètres]
-- Type énuméré : on utilise '|' pour faire l'union des ensembles de valeurs.
data CouleurCarte = Trefle | Carreau | Coeur | Pique

-- Type tuple : on utilise l'espace pour faire le produit cartésien des ensembles de valeurs.
-- Carte = {Trefle, Pique...} x {2,3,..., As}
data Carte = cte CouleurCarte ValeurCarte
 
-- Type (tuple) polymorphe : composé d'au moins une famille de type
data Point a = Point a a

-- Type (énuméré) polymorphe : cercle défini par un centre de type Point a et d'un rayon de type a...
data Shape a = Circle (Point a) a | Rectangle (Point a) (Point a)
 
-- Type récursif : exemple sur Tree et NestedList
data Tree a = Leaf a | Node (Tree a) (Tree a)

flatten :: Tree a -> [a]    -- fonction qui met toutes les valeurs de l'arbre dans un tableau
flatten tree = f tree []
  where f t lst = case (t, lst) -> x:lst of
                    (Leaf x, lst) -> x:lst
                    (Node l r, lst) -> f l (f r lst)
 
 treeHeight :: Tree a -> Int
 treeHeight tree = case tree of
                    (Leaf _) -> 1
                    (Node tl tr) -> 1 + max (treeHeight tl) (treeHeight tr)
 
let t = (Node (Node (Leaf 'a') (Leaf 'b')) (Leaf 'c'))


data NestedList a = Elem a | List [NestedList a]

flatten :: NestedList a -> [a]
flatten nl = case nl of
               (Elem x) -> [x]
               (List []) -> []
               (List (x:xs)) -> flatten x ++ flatten (List xs)

flatten' :: NestedList a -> [a]
flatten' nl = f nl []
  where f nl res = case (nl,res) of
                     (Elem x,ys) -> x:ys
                     (List l,ys) -> foldr f ys l
 
