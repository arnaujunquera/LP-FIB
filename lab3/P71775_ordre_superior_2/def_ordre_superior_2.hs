countIf :: (Int -> Bool) -> [Int] -> Int
countIf f l = countIf' f l 0
  where
    countIf' :: (Int -> Bool) -> [Int] -> Int -> Int
    countIf' _ [] count = count
    countIf' f (x:xs) count
      | f x       = countIf' f xs (count+1)
      | otherwise = countIf' f xs count

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam _ [] = []
pam l (f:fs) = [(map f l)] ++ (pam l fs)

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 [] _ = []
pam2 (x:xs) f = [(pam2' x f)] ++ (pam2 xs f)
  where
    pam2' :: Int -> [Int -> Int] -> [Int]
    pam2' _ []      = []
    pam2' x (f:fs)  = [f x] ++ pam2' x fs

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl _ _ x0 [] = x0
filterFoldl cond f x0 (x:xs)
  | (cond x)  = filterFoldl cond f (f x0 x) xs
  | otherwise = filterFoldl cond f x0 xs

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert _ [] x0 = [x0]
insert cond l0 x0 = insert' cond l0 x0 []
  where
    insert' :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int] -> [Int]
    insert' cond (x:xs) x0 l
      | (cond x0 x) = x0:(x:xs)
      | otherwise   = x:(insert' cond xs x0 l)

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort _ [] = []
insertionSort cond l = foldl (insert cond) [] l
