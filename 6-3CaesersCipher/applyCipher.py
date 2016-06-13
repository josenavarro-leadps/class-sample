import string

# applyCipher.py
# A proramm to encrypt/decrypt user text
# using Caesar's Cipher

# Author: rc.navarro.jose

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	ALPHABET = string.ascii_uppercase
	alphabet = string.ascii_lowercase
	dictionary = {}
	for x in range(0, len(alphabet)):
		dictionary[ALPHABET[(x + key) % 26]] = ALPHABET[x]
	for x in range(0, len(alphabet)):
		dictionary[alphabet[(x + key) % 26]] = alphabet[x]
	for x in range(32, 64):
		dictionary[chr(x)] = chr(x)
	return dictionary

# the encoded messag from user 
def getMessage():
	print("Welcome, what message would you wat to encode?")
	message = raw_input()
	return message


def decodeMessage(message, Dictionary):
	theMessage = ""
	for y in message:
		theMessage = theMessage + Dictionary[y]
	return theMessage

# outputs the message to the terminal
# arguements: decoded message
# returns: none
def printMessage(message):
	print(message)


# execution starts here

# ask user for key
try:
	print("What key do you want to use")
	key = int(raw_input())

	Dictionary = createDictionary(key)
	encodedMessge = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("Here is the message coded")
	printMessage(decodedMessage)

except:
	print("Sorry, seems like you did a mistake")




