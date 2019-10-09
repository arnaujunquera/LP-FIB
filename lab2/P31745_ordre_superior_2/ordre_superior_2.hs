flatten :: [[Int]] -> [Int]
flatten = foldr (++) []

myLength :: String -> Int
myLength [] = 0
myLength x = last $ zipWith (f) x (iterate (+1) 1)
    where f a b = b

countIn :: [[Int]] -> Int -> [Int]
countIn l x = map (f x) l
    where f a b = length $ filter (== a) b

firstWord :: String -> String
firstWord x = takeWhile (/= ' ') (dropWhile (== ' ') x)
