# a program for keeping track of used cars problem designed by mflax@leadps.org
 
# represents a single car
class Car(object):
    # every car has a make, model, year, and color
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
 
    # prints the ad for this car to the terminal
    def ad(self):
        print("Buy this beautiful " + self.color + " " + str(self.year) + " " + self.make + " " +self.model + 
"!")
 
 
# takes a list of Car objects and prints the ad for all of them
def printAds(carList):
    for c in carList:
        c.ad()
 
# THE loadCars FUNCTION IS FOR YOU AND YOUR PARTNER TO IMPLEMENT takes a list to fill with Car objects and a 
# filename for saved Cars opens the file, creates new Car objects and adds them to the list
 
# note that you can pass a list and that the things you add to it will be there after calling this function 
# this isn't true in every language!!
def loadCars(my_name, filename, list):
    # open the file
	myLine = my_name.readline()
	while myLine != '': 
 		myWords = myLine.split()
		car = Car(myWords[0], myWords[1], myWords[2], myWords[3])
		list.append(car)
		myLine = my_name.readline()
    # read each line from the file for each one, pull apart the variables to create a Car object
    # close the file
     # placeholder
 
 
 
# execution starts here!
 
# here's an empty list that we'll fill with cars
ourCars = []
 
# we'll add this car to start as an example of adding a car to our list
cars = ourCars.append(Car('Honda', 'Fit', '2009', 'Grey'))
 
# here you load the list of cars

print("Hey user, what's the filename of your car list?")
name = raw_input()
my_file = open('myCars.txt', 'r') 
loadCars(my_file, 'myCars.txt', ourCars)
my_file.close()
# now we'll walk through the list
printAds(ourCars)
my_file.close()
