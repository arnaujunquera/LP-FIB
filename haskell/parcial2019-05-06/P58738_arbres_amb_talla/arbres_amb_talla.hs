data STree a = Nil | Node Int a (STree a) (STree a)
  deriving Show

div10 = flip div 10
t1 = Node 3 99 (Node 1 88 Nil Nil) (Node 1 22 Nil Nil)
t2 = Node 2 77 (Node 1 33 Nil Nil) Nil
t3 = Node 6 44 t1 t2
t4 = Node 7 55 t1 t2

size :: STree a -> Int
size Nil = 0
size (Node _ _ lt rt) = 1 + size lt + size rt

isOk :: STree a -> Bool
isOk Nil = True
isOk (Node s _ lt rt) = correctNode && isOk lt && isOk rt
  where
    correctNode = s == (size lt + size rt) + 1

-- not workings
-- nthElement :: STree a -> Int -> Maybe a
-- nthElement Nil _ = Nothing
-- nthElement (Node s n lt rt) x
--   | x <
--
-- mapToElements :: (a -> b) -> STree -> [Int] -> [Maybe b]
-- mapToElements _ Nil _ = Nothing
-- mapToElements f (Node s n lt rt) l =

instance Functor STree where
  fmap f Nil              = Nil
  fmap f (Node s n lt rt) = (Node s (f n) (fmap f lt) (fmap f rt))
