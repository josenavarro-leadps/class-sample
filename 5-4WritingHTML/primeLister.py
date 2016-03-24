def isPrime(myNum):
	for numbers in range(2,myNum):
		if myNum % numbers == 0:
			return False
		return True

List = []

for numbers in range (2,10000):
	n = isPrime(numbers)
	if n == True:
		List.append(numbers)
myFile = open("thePrimes.txt", "w")
myFile.write(str(List))
myFile.close()
print(List)
