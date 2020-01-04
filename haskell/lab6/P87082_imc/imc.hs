-- ================================== BMI =================================== --

bmi :: [String] -> String
bmi [name, weight, heigth] = name ++ ": " ++ bmi'
  where
    bmi' :: String
    bmi'
      | imc <  18 = "underweight"
      | imc <= 25 = "normal weight"
      | imc <= 30 = "overweight"
      | imc <= 40 = "obese"
      | otherwise = "severely obese"
      where
        imc :: Float
        imc = w / (h ^ 2)
          where
            h, w :: Float
            h = read heigth
            w = read weight

-- ================================= OUTPUT ================================= --

output :: String -> String
output [] = ""
output str = bmi $ words str

-- ================================== MAIN ================================== --

main :: IO ()
main = do
  input <- getLine
  if (input /= "*") then do
    putStrLn $ output input
    main
  else
    return ()
