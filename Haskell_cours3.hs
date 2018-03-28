foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f z [] = z
foldr f z (x:xs) = f x (foldr z f xs)

-- Application à la fonction reverse
myReverse lst = foldl sort 0 lst
