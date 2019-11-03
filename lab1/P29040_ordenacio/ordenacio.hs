insert :: [Int] -> Int -> [Int]
insert [] i = [i]
insert (x:xs) i
  | i > x     = x:(insert xs i)
  | otherwise = i:(x:xs)

isort :: [Int] -> [Int]
isort l = isort' l []
  where
    isort' :: [Int] -> [Int] -> [Int]
    isort' [] l'       = l'
    isort' (x:xs) l'  = isort' xs (insert l' x)

remove :: [Int] -> Int -> [Int]
remove [] _ = []
remove (x:xs) r
  | r /= x    = x:(remove xs r)
  | otherwise = xs
