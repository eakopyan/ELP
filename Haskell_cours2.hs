-- Expression let ou clause where : permettent de se référer localement à une valeur intermédiaire

split lst n = case (lst, n) of 
  ((x:xs), n)  -- les ":" servent à concaténer
    | n > 0 -> let (f, l) = split xs (n-1) in (x:f, l)
  (xs, n) -> ([], xs)
  
-- ou :

split lst n = case (lst, n) of
  ([], n) -> ([], [])
  ((x:xs), n)
    | n > 0 -> (x:ys, zs)
    | otherwise -> ([], x:xs)
    where (ys, zs) = split xs (n-1)


-- Ex : définir la fonction qui encode une suite de n éléments égaux à x par le tuple (n, x)
encode :: (Eq a) => [a] -> [(Int, a)]
encode lst = case lst of
  [] -> [] -- si liste vide, on renvoie une liste vide
  (x:xs) -> case res of  -- res défini à la fin grâce à la clause where
    [] -> [(1, x)]
    (y:ys) -> case y of
      (nb, elem)
        | elem == x -> (nb+1, x):ys
        | otherwise -> (1, x):res  -- concaténé à l'ensemble du résultat
    where res = encode xs


-------------------------------------------------------------------------------------------

-- Principe de paresse : expressions non évaluées tant que leurs valeurs ne sont pas requises.
-- Ex : x = 1/0 ne renvoie pas d'erreur tant qu'on utilise pas x !
-- La paresse implique la pureté, donc pas d'effet de bord (évaluation d'une expression sur l'extérieur)

-- Défi 1: tracer une évaluation (les fonctions sont arbitraires et servent juste à illustrer...)

repeat x = x : repeat x

take n list = case (n, lst) of
  (n, _)  -- "_" est un joker quand on veut pas préciser la valeur d'un paramètre
    | n <= 0 -> []
  (_, []) -> []
  (n, (x:xs)) -> x: take (n-1) xs
  
-- Evaluation :
-- take 3 (repeat 7) = take 3 (7: repeat 7) = 7: take (3-1) (repeat 7) = 7: take 2 (repeat 7)
-- = 7: take 2 (7: repeat 7) = 7:7: take (2-1) (repeat 7) = ... = 7:7:7:[]
-- Conclusion : repeat x renvoie une liste infinie de x, et take n ne prend que les n premiers éléments
-- Tracer une évaluation permet aussi d'estimer la complexité d'un code

-- Défi 2 : 
myReverse xs = rev xs []
  where rev lst reversed = case (lst, reversed) of
    ([], reversed) -> reversed
    ((x:xs), reversed) -> rev xs (x:reversed)
    
-- Complexité :
-- myReverse [1,2,3,4] = rev [1,2,3,4] [] = rev [2,3,4] 1:[] = rev [3,4] 2:1:[] 
-- = ... = 4:3:2:1:[]

-- Syntaxe : f(g(x)) s'écrit en Haskell : f . g

-- Défi 3 : filter
group :: (Eq a) => [a] -> [[a]]
group lst = case lst of
  [] -> []
  (x:xs) -> (x: (filter (==x) xs)) : (group (filter (/=x) xs)) -- /= signifie "différent de"
-- on prend x, puis tous les éléments égaux à x, puis on rappelle la fonction sur les éléments restants

-- Défi 4 : map
encode :: (Eq a) => [a] -> [(a, Int)]
encode lst = case lst of
  [] -> []
  (x:xs) -> map (\x -> (head x, length x)) (group lst)  -- \x signifie qu'on associe qch à chaque x
  
  
-- Liste en extension
-- { f(x) | x in xs, x < k} s'écrit en Haskell : [f x | x <- xs, x<k]
  
quicksort lst = case lst of
  [] -> []
  (x:xs) -> quicksort [y | y <- xs, y<x] ++ x ++ quicksort [y | y <- xs, y >= x]

  
