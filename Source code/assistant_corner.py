import random
def jokes():
	f = open(joke.txt)
	content = f.read()
	jokes = content.split('\n\n')
	return str(random.choice(jokes))

def greet():
	return "Vivek, online; your personal virtual assistant. How can I help you."
