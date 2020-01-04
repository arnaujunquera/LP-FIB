flatten :: [[Int]] -> [Int]
flatten = foldr (++) []

myLength :: String -> Int
myLength [] = 0
myLength x = last $ zipWith (\a b -> b) x (iterate (+1) 1)

myReverse :: [Int] -> [Int]
myReverse a = foldr (\x y -> y++[x]) [] a

countIn :: [[Int]] -> Int -> [Int]
countIn l x = map (f x) l
    where f a b = length $ filter (== a) b

firstWord :: String -> String
firstWord x = takeWhile (/= ' ') (dropWhile (== ' ') x)
