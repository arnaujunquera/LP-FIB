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
isOk (Node n _ lt rt) = correctNode && isOk lt && isOk rt
  where
    correctNode = n == (size lt + size rt) + 1
