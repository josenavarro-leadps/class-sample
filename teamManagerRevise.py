
#made a class that contains the goals, age, and name. "self" is always being needed
class player(object):
        def __init__(self, goals, age, name):
                self.goals = goals
                self.age = age
                self.name = name
#now I made a function in my class
        def playerstats(self):
                print("name:" + self.name)
                print("goals:" + self.goals)
                print("age:" + self.age)
#empty list to add on to
myPlayers = []                                                                                                        
#made print statements to let the user know that there is three options
while 3 > 1:                                                                                                          
        print("If you want to add a player press 1")
        print("If you want to copy a player press 2")
        print("Press 3 to exit")                                                                                      
        choice = int(raw_input()
# asks the user for data if they chose number 1 data: name, age, goals
        if choice == 1:
                #asks for the name of the player
                print("whats the new members name")
                name = str(raw_input())                                                                               
                #asks for age
                print("How old is the new player")
                age = str(raw_input())
                #asks for goals scored in lifetime
                print("How many goals did the new player make")
                goals = str(raw_input())
                #adds the new player to the list                                                                      
                myPlayers.append(player(name, age, goals))
                                                                                                                      
#will copy the the goals, age, and ,name
        elif choice == 2:                                                                                             
                for status in myPlayers:                                                                              
                                status.playerstats()
# asks what you want to do                                                                                            
        elif choice == 3:                                                                                             
                exit()
