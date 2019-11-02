ones :: [Integer]
ones = repeat 1


nats :: [Integer]
nats = iterate (+1) 0


ints :: [Integer]
ints = tail $ concat $ map (f) nats
  where
    f x = [x, -x]


triangulars :: [Integer]
triangulars = tail $ scanl (+) 0 nats


factorials :: [Integer]
factorials = scanl (*) 1 [1..]


fibs :: [Integer]
fibs = 0 : 1 : (zipWith (+) fibs (tail fibs))


isPrime :: Integer -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n = isPrime' 2
  where
    isPrime' :: Integer -> Bool
    isPrime' d
      | mod n d == 0    = False
      | d == (div n 2)  = True
      | otherwise       = isPrime' (d + 1)

primes :: [Integer]
primes = filter isPrime nats

isHamming :: Integer -> Bool
isHamming 0 = False
isHamming 1 = True
isHamming 2 = True
isHamming 3 = True
isHamming 5 = True
isHamming n = isHamming' n
  where
    isHamming' :: Integer -> Bool
    isHamming' n
      | mod n 2 == 0 || mod n 3 == 0 || mod n 5 == 0 = True
      | otherwise = False

hammings:: [Integer]
hammings = filter isHamming nats



lookNsay :: [Integer]
lookNsay = iterate count 1

count :: Integer -> Integer
count a = read $ next $ show a

next :: [Char] -> [Char]
next [] = []
next cs = (show n) ++ [pr] ++ next cua
  where
    pr = head cs
    n = length $ takeWhile ( == pr) cs
    cua = dropWhile ( == pr) cs



tartaglia :: [[Integer]]
tartaglia = (iterate (pascal) [1])

pascal :: [Integer] -> [Integer]
pascal xs = zipWith (+) (xs ++ [0]) ([0] ++ xs)
