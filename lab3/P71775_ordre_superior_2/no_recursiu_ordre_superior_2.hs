countIf :: (Int -> Bool) -> [Int] -> Int
countIf f l = length $ filter f l

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam l fs = [map f l | f <- fs]

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 l fs = [[f x | f <- fs] | x <- l]

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl cond f x0 l = foldl f x0 $ filter cond l

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert _ [] x0 = [x0]
insert cond l0 x0 = insert' cond l0 x0 []
  where
    insert' :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int] -> [Int]
    insert' cond (x:xs) x0 l
      | (cond x0 x) = x0:(x:xs)
      | otherwise   = x:(insert' cond xs x0 l)

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort cond l = foldr (\x xs -> insert cond xs x) [] l
