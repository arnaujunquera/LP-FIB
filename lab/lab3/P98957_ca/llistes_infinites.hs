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
