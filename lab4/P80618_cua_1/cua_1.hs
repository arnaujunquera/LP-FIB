data Queue a = Queue [a] [a]
	deriving (Show)

c = push 3 (push 2 (push 1 create))


create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push a (Queue l1 l2) = Queue l1 (a:l2)

pop :: Queue a -> Queue a
pop (Queue [] l2) = pop $ Queue (reverse l2) []
pop (Queue (x:l1) l2) = Queue l1 l2

top :: Queue a -> a
top (Queue [] l2) = last l2
top (Queue (x:l1) l2) = x

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty (Queue l1 l2) = False