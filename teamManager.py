#made a class that contains the goals, age, and name.
#"self" is always being needed
class player(object):
	def __init__(self, goals, age, name):
                self.goals = goals
                self.age = age
                self.name = name
#now I made a function in my class
	def playerstats(self):
		print("name" + self.name)
        	print("goals" + self.goals)
		print("age" + self.age)
#empty list to add on to
myPlayers = []
#made print statements to let the user know that there is three options
print ("If you want to add a plyer press 1")
print ("If you want to copy a player press 2")
print ("Press 0 to exit")
choice = int(input())

while choice != 0:

# asks the user for data if they chose number 1
#data: name, age, goals

	if choice == "1": 
		print ("whats the new members name")		
		name = input()
		#name of memeber
		print ("How old is the new player")
		age = input()
		#asks for age
		print ("How many goals did the new player make")
		goals = input()
		#goals in life time
		#adds the new player to the list
		myPlayers.append(player(name, age, goals))
		print ("Do you want to keep adding players, or do you want to copy all players")
		choice = input()
#will copy the the goals, age, and ,name
	elif choice == "2":
		for status in myPlayers:
			status.playerStats()
# asks what you want to do
		print ("choose again, 1:add a new player to the squad, 2:copy status from players")
		choice = input()
