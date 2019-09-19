-- P77907

absValue :: Int -> Int
absValue n
  | n >= 0 = n
  | otherwise = -n


power :: Int -> Int -> Int
power x 0 = 1
power x n = x * power x (n - 1)


isPrime :: Int -> Bool
isPrime 2 = True
isPrime n = isPrime' 2
  where
    isPrime' :: Int -> Bool
    isPrime' d
      | mod n d == 0    = False
      | d == (div n 2)  = True
      | otherwise       = isPrime' (d + 1)


slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2)
