myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ x [] = x
myFoldl f x (y:ys) = myFoldl f (f x y) ys

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ x [] = x
myFoldr f x (y:ys) = f y (myFoldr f x ys)

myIterate :: (a -> a) -> a -> [a]
myIterate f x = x : myIterate f (f x)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil b f x
  | b x == False = myUntil b f (f x)
  | otherwise = x

myMap :: (a -> b) -> [a] -> [b]
myMap f xs = [f x | x <- xs]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f xs = [x | x <- xs, f x]

myAll :: (a -> Bool) -> [a] -> Bool
myAll f x = and $ map (\x-> f x) x

myAny :: (a -> Bool) -> [a] -> Bool
myAny f x = or $ map (\x-> f x) x

myZip :: [a] -> [b] -> [(a, b)]
myZip _ [] = []
myZip [] _ = []
myZip (x:xs) (y:ys) = (x, y) : myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = [f x y | (x, y) <- myZip xs ys]
