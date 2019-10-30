divisors :: Int -> [Int]
divisors x = [d | d <- [1..x], mod x d == 0]

nbDivisors :: Int -> Int
nbDivisors = length . divisors

moltCompost :: Int -> Bool
moltCompost x = and [r | y <- [1..(x-1)], let r = nbDivisors y < nbDivisors x]
