convert :: String -> String
convert s =
  if (last s) == 'a' || (last s) == 'A' then
    "Hola maca!"
  else
    "Hola maco!"


main :: IO ()
main = do
  name <- getLine
  putStrLn $ convert name
