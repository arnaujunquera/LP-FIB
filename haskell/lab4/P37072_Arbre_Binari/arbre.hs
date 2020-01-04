data Tree a = Node a (Tree a)(Tree a) | Empty
  deriving(Show)

t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2

size :: Tree a -> Int
size Empty = 0
size (Node _ lT rT) = size lT + size rT + 1


height :: Tree a -> Int
height Empty = 0
height (Node _ lT rT) = (max (height lT) (height rT)) + 1

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty = True
equal (Node x lX rX) (Node y lY rY)
  | x == y = (equal lX lY) && (equal rX rY)
  | otherwise = False

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node n lT rT) = n : ((preOrder lT) ++ (preOrder rT))

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node n lT rT) = (postOrder lT) ++ (postOrder rT) ++ [n]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node n lT rT) = (inOrder lT) ++ [n] ++ (inOrder rT)

breadthFirst :: Tree a -> [a]
breadthFirst t = bf [t]
  where
    bf [] = []
    bf (Empty : xs) = bf xs
    bf ((Node n lT rT) : xs) = (n : bf ([lT] ++ [rT]))
