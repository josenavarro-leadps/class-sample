# applyCipher.py
# A proramm to encrypt/decrypt user text
# using Caesar's Cipher

# Author: rc.navarro.jose

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):


	#placeholder
	return {}

# the encoded messag from user 
def getMessage():
	pass	

# for each letter in message, decodes and records 
# arguements: encoded messae, dictionary
#returns: decoded message
def decodeMessage(message, dictionary):
	pass

# outputs the message to the terminal
# arguements: decoded message
# returns: none
def printMessage(message):
	pass


# 4execution starts here

# ask user for key
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessge = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)
printMessage(decodedMessage)

