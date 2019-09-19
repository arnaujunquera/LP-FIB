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

average :: [Int] -> Float
average [x] = x
average (x:xs) = div mySum [y] myLength [u]
  where
    mySum :: [Int] -> Int
    mySum [x] = x
    mySum (x:xs) = x + mySum xs
