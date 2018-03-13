-- Type Haskell expressions in here.

λ 5+7
-- 12:: Num a => a
λ "loic"
-- "loic":: [Char]
λ [42,13,22]
-- [42,13,22]:: Num t => [t]

-- functions (sort, fst, map, filter)
λ sort [42,13,22]
-- [13,22,42]:: (Num a, Ord a) => [a]
λ sort "chris"
-- "chirs":: [Char]
λ (28, "chirs")
-- (28,"chirs"):: Num t => (t, [Char])
λ fst (28, "chirs")
-- 28:: Num a => a

-- variable declarations
λ let x = 4 in x*x
-- 16:: Num a => a
λ let x = 8*10 in x+x
-- 160:: Num a => a

-- select output (in)
λ let villain = (28, "chirs") in fst villain
-- 28:: Num a => a
λ 'a' : []
-- "a":: [Char]
λ 'a':'b':[] == ['a','b']
-- True:: Bool
λ ['a','b','c'] == "abc"
-- True:: Bool

-- apply functions on lists
λ map (+1) [1..5]
-- [2,3,4,5,6]:: (Enum b, Num b) => [b]
λ map (*99)[1..10]
-- [99,198,297,396,495,594,693,792,891,990]:: (Enum b, Num b) => [b]
λ map (/5)[13,24,50,42]
-- [2.6,4.8,10.0,8.4]:: Fractional b => [b]
λ filter (>5)[62,3,25,7,1,9]
-- [62,25,7,9]:: (Num a, Ord a) => [a]
λ (1, "George")
-- (1,"George"):: Num t => (t, [Char])
λ map (/5) [13,24,52,42]
-- [2.6,4.8,10.4,8.4]:: Fractional b => [b]
λ 1 : [2,3]
-- [1,2,3]:: Num a => [a]

-- definition of functions
λ let square x = x*x in square 52
-- 2704:: Num a => a
λ let add1 x = x+1 in add1 5
-- 6:: Num a => a
λ let second x = snd x in second (3,4)
-- 4:: Num b => b
λ let square x = x*x in map square [1..10]
-- [1,4,9,16,25,36,49,64,81,100]:: (Enum b, Num b) => [b]
λ let add1 x = x+1 in map add1 [1,5,7]
-- [2,6,8]:: Num b => [b]
λ let take5s = filter (==5) in take5s [1,5,2,5,3,5]
-- [5,5,5]:: (Eq a, Num a) => [a]
λ let take5s = filter (==5) in map take5s [[1,5],[5],[1,1]]
-- [[5],[5],[]]:: (Eq a, Num a) => [[a]]

-- functions on char
λ toUpper 'a'
-- 'A':: Char
λ map toUpper "Chris"
-- "CHRIS":: [Char]

-- select output, pt2
λ let (a,b) = (10,12) in a*2
-- 20:: Num a => a
λ let (a:b:c:[]) = "xyz" in a
-- 'x':: Char
λ let (a:_:_:_) = "xyz" in a
-- 'x':: Char
λ let (a:_) = "xyz" in a
-- 'x':: Char

λ let (_,(a:_)) = (10,"abc") in a
-- 'a':: Char
λ let _:_:c:_ = "abcd" in c
-- 'c':: Char
λ let [a,b,c] = "cat" in (a,b,c)
-- ('c','a','t'):: (Char, Char, Char)
λ let abc@(a,b,c) = (10,20,30) in (abc,a,b,c)
-- ((10,20,30),10,20,30):: (Num t, Num t1, Num t2) => ((t, t1, t2), t, t1, t2)
