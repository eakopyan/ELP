import System.Environment -- for getArgs

isSorted lst = case lst of
                 [] -> True
                 [x] -> True
                 (x:xs@(y:ys)) -> (x <= y) && (isSorted xs)  
                
dupli :: [a] -> [a]                
                
dupli lst = case lst of
                [] -> []
                (x:xs) -> x:(x:(dupli xs))

main = do
  args <- getArgs
  putStrLn ( (show args)
             ++ " is sorted ? "
             ++ show (isSorted args) )
