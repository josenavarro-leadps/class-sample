contact = {

}

while 7 > 0:	
	print("What would you like to do now")
	print("(1) Add a phone number")
	print("(2) Print the full lst of contacts")
	print("(3) Enter a name to retrieve that contact's phone number")
	print("(0) Exit the contacts app")
	answer = int(raw_input())
	if answer == 1:
		print("Enter contact name:")
		desicion = str(raw_input())
		print("Enter number:")
		number = str(raw_input())
		contact[desicion] = number

	elif answer == 2:
		print("Contacts:")
		print(contact)
	elif answer == 3:
		print("retreive:")
		print("Type Name")
		choice = raw_input()
		print("Here is the contact information")
		print(contact[choice])
	elif answer == 0:
		exit()
		




