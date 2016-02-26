class  Quote(object):	
	def __init__(self, qoute_text, user_posted, location, num_likes):
		self.quote_text = quote_text
		self.user_posted = user_posted
		self.location = location
		self.num_likes = num_likes
# adds one to the 'like' count
	def like(self):
		self.num_likes = self.num_likes + 1
	
	def nun_like(self):	
		self.num_likes = self.num_likes - 1
	
	def show_quote(self):
		print("U: " + user_posted)
		print("L: " + location)
		print("Quote: " + quote_text)
		print("likes: " + str(self.num_likes))

x = Quote("Nothing with Shawn.", "kevin_is_kool", "San Francisco", 0)
y = Quote("If I wasn't crazy, I'd be insane.","me", "The Edge of The World", 0) 
z = Quote("Barca raw", "jose", "Mexico", 0)

z.show_quote

#put quotes in a list
my_quotes = []
my_quotes.append(x)
my_quotes.append(y)
my_quotes.append(z)
user_quotes = "Hello. How are you?"
speaker = "Adele"
location ="London"

myquotes.append(Quote(user_quote, speaker, location, 0))
# call our show_quote function for all of our Quote objects
for q in my_quotes:
	q.show_quote()
