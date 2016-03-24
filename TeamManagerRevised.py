class player(object):
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	def playerstats(self):
		print("name:" + self.name)
		print("age:" + self.age)
		print("goals:" + self.goals)
myPlayers = []

while 3 > 1:
	print("If you want to add a player press 1")
	print("If you want to copy a playerpress 2")
	print("Press 3 to exit")
	choice = int(raw_input())	

	if choice == 1:
		print("What is the new members name") 
		name = str(raw_input())
		print("How old is the new player")
		age = str(raw_input())
		print("How many goals did the new player make")
		goals = str(raw_input())
		myPlayers.append(player(name, age, goals))
	elif choice == 2:
		for status in myPlayers:
			status.playerstats()
	elif choice == 3:
		exit()
