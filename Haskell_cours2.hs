-- Expression let et clause where

split lst n = case (lst, n) of ((x:xs), n)
| n>° -> let (f, l) = split xs (n-1) in (x:f, l)
