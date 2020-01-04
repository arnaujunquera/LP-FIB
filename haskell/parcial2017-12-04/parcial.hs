-- Problema 1: Expressio postfixa 1 --
eval1 :: String -> Int
eval1 s = eval1' (words s) []
  where
    eval1' :: [String] -> [Int] -> Int
    eval1' [] [r]   = r
    eval1' (w:ws) p
      | w == "*"  = eval1' ws ((*) (head $ tail p) (head p)):(tail $ tail p)
      | w == "+"  = eval1' ws ((+) (head $ tail p) (head p)):(tail $ tail p)
      | w == "-"  = eval1' ws ((-) (head $ tail p) (head p)):(tail $ tail p)
      | w == "/"  = eval1' ws ((head $ head p) / (head p)):(tail $ tail p)
      | otherwise = eval1' ws w:p
--
-- -- Problema 2: Expressio postfixa 2 --
-- eval2 :: String -> Int
-- eval2 s = [x | w <- (words s), ]

-- Problema 3: fsmap
fsmap :: a -> [a -> a] -> a
fsmap x []      = x
fsmap x (f:fs)  = fsmap (f x) fs

-- Problema 4: Dividir i vèncer --
-- divideNconquer :: (a -> Maybe b) -> (a -> (a, a)) -> (a -> (a, a) -> (b, b) -> b) -> a -> b

-- Probma 5: Racionals --
data Racional = Racional Integer Integer

racional :: Integer -> Integer -> Racional
racional num den = Racional (div num mcd) (div den mcd)
  where
    mcd = gcd num den

numerador :: Racional -> Integer
numerador (Racional num den) = num

denominador :: Racional -> Integer
denominador (Racional num den) = den

instance Eq Racional where
  Racional num1 dem1 == Racional num2 dem2 = num1 == num2 && dem1 == dem2

instance Show Racional where
  show (Racional num den) = show num ++ "/" ++ show den


-- Problema 6: Arbre de Calkin-Wilf
data Tree a = Node a (Tree a) (Tree a)

recXnivells :: Tree a -> [a]
recXnivells t = recXnivells' [t]
  where
    recXnivells' ((Node x fe fd):ts) = x:recXnivells'(ts++[fe,fd])

rationalsTree :: Racional -> Tree Racional
rationalsTree (Racional a b) = (Node (Racional a b) fe fd)
  where
    fe = rationalsTree (Racional a (a+b))
    fd = rationalsTree (Racional (a+b) b)

racionals :: [Racional]
racionals = recXnivells (rationalsTree (Racional 1 1))
