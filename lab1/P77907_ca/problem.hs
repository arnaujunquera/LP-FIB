-- P77907

absValue :: Int -> Int
absValue n
  | n >= 0 = n
  | otherwise = -n


power :: Int -> Int -> Int
power x 0 = 1
power x n = x * power x (n - 1)

--
-- isPrime :: Int -> Bool
-- isPrime 2 = True
-- isPrime n = isPrime' 2
--   where
--     isPrime' :: Int -> Bool
--     isPrime' d
--       | mod n d == 0    = False
--       | d == (div n 2)  = True
--       | otherwise       = isPrime' (d + 1)

isPrimeRec :: Integer -> Integer -> Bool
isPrimeRec x div
    | div == 1 = True
    | x `mod` div == 0 = False
    | otherwise = isPrimeRec x (div - 1)

isPrime :: Integer -> Bool
isPrime x
    | x == 0 = False
    | x == 1 = False
    | otherwise = isPrimeRec x (floor (sqrt (fromIntegral x)))


slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2)

quickFib :: Int -> Int
quickFib 0 = 0
quickFib 1 = 1
quickFib n = quickFib' 0 1 2
  where
    quickFib' :: Int -> Int -> Int -> Int
    quickFib' first second it
      | it == n = first + second
      | otherwise = quickFib' second (first + second) (it + 1)
