myLength :: [Int] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs



myMaximum :: [Int] -> Int
myMaximum [x] = x
myMaximum (x:xs)
  | x > max = x
  | otherwise = max
  where
    max = myMaximum xs



intToFloat::Int -> Float
intToFloat n = fromInteger (toInteger n)

average :: [Int] -> Float
average [x] = intToFloat x
average (x:xs) = intToFloat (x+sum xs) / intToFloat (1 + myLength xs)
  where
    sum :: [Int] -> Int
    sum [] = 0
    sum (x:xs) = x + sum xs



buildPalindrome :: [Int] -> [Int]
buildPalindrome [] = []
buildPalindrome x = reverse x ++ x
  where
    reverse :: [Int] -> [Int]
    reverse [x] = [x]
    reverse (x:xs) = reverse xs ++ [x]



inside :: [Int] -> Int -> Bool
inside [y] x = y == x
inside (y:ys) x = (y == x) || inside ys x

remove :: [Int] -> [Int] -> [Int]
remove [] [] = []
remove [] y = []
remove x [] = x
remove (x:xs) y
    | not (inside y x)  = (x:(remove xs y))
    | otherwise         = remove xs y



flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ flatten xs



oddList :: [Int] -> [Int]
oddList [] = []
oddList (x:xs)
  | (mod x 2) == 0  = (x:(oddList xs))
  | otherwise       = oddList xs

evenList :: [Int] -> [Int]
evenList [] = []
evenList (x:xs)
  | (mod x 2) == 0  = evenList xs
  | otherwise       = (x:(evenList xs))

oddNevens :: [Int] -> ([Int],[Int])
oddNevens [] = ([],[])
oddNevens x = ((evenList x), (oddList x))



-- isPrime :: Int -> Bool
-- isPrime 2 = True
-- isPrime n = isPrime' 2
--   where
--     isPrime' :: Int -> Bool
--     isPrime' d
--       | mod n d == 0    = False
--       | d == (div n 2)  = True
--       | otherwise       = isPrime' (d + 1)
--
-- primeDivisors :: Int -> [Int]
-- primeDivisors 1 = []
-- primeDivisors n = primeDivisors' 2
--   where
--     primeDivisors' :: Int -> [Int]
--     primeDivisors' d
--       | d > n = []
--       | ((mod n d) == 0) && isPrime d = (d:(primeDivisors' (d+1)))
--       | otherwise                     = primeDivisors (d+1)
