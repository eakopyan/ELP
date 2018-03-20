-- Compilation avec un main : 
-- ghc fichier.hs -o executable
-- ./executable

-- Compilation sans main :
-- ghci fichier.hs

import System.Environment -- for getArgs

-- Vérification de l'ordre dans une liste
isSorted lst = case lst of
                 [] -> True  -- flèche simple pour définir une association ( => pour indiquer le contexte)
                 [x] -> True
                 (x:xs@(y:ys)) -> (x <= y) && (isSorted xs)  
   
-- Duplication du premier élément d'une liste   
dupli :: [a] -> [a]       -- fonction qui prend en param un tableau et renvoie un tableau                         
dupli lst = case lst of
                [] -> []
                (x:xs) -> x:(x:(dupli xs))
                
addElemList x c lst
  | c <= 0 = lst  
  | c > 0 = addElemList x (c-1) (x:lst)
                
repli :: [a] -> Int -> [a]
repli lst c = case (lst, c) of
                ([], c) -> []
                ((x:xs), c) -> addElemList x c (repli xs c)
            
-- Supprimer deux éléments successifs d'une liste           
compress :: (Eq a) => [a] -> [a]
compress lst = case lst of
                [] -> []
                [x] -> [x]
                (x:x':xs)
                  | x == x' -> compress (x':xs)  -- SI x = x' ALORS ....
                  | otherwise -> x:(compress(x':xs))  -- SINON on ajoute x au résultat de compress(x':xs)
                  

-- fonction main du programme Haskell
main = do
  args <- getArgs
  putStrLn ( (show args)  -- affichage sur le terminal
             ++ " is sorted ? "
             ++ show (isSorted args) )
