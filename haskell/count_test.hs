
f x = sqrt (x * x + x * 2.0 + 3.0)

main = do
	print (map f [0..1000])
