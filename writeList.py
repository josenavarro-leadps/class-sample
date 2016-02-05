myFile = open("numList.txt","w")
#createa list to write to my file
nums = range(1,501)
# write each item to thefile
for n in nums:
	myFile.write(str(n) + '\n')
myFile.close()
