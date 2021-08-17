# I hereby confirm that I do not communicate with other people than the teacher of
# the course during the exam.
# I am aware that cheating in the exam may lead to disciplinary measures


# Question 1: Pandemic Rules

def norway_pandemic():
	a = input("Hvor er du bosatt?")
	if(a.lower()[0] == 'v'):
		velkommen()
		return
	a = input("Er du fullvaksinert?")
	if(a.lower() == 'ja'):
		velkommen()
		return
	a = input("Har du gjennomgått koronasykdom de siste seks månedene?")
	if(a.lower() == 'ja'):
		velkommen()
		return
	velkommen(True)

def velkommen(teste = False):
	if(teste):
		print("Velkommen til Norge, men du må teste deg och sitte i karantene.")
	else:
		print("Velkommen til Norge!")

# Question 2: Scrambled text

def alter(s):
	a = ""
	for i in range(1, len(s), 2):
		a += s[i]
		a += s[i-1]
	if(len(a) < len(s)):
		a += s[-1]
	return a

def scramble(s):
	if(len(s) < 4):
		return s
	a = alter(s[1:-1])
	return s[0] + a + s[-1]

def scrambles(s):
	a = ""
	for word in s.split():
		a += scramble(word) + " "
	return a[0:-1]

# Question 3: Bank accounts

class Account:
	def __init__(self, number, balance):
		self.number = number
		self.balance = balance

	def get_balance(self):
		return self.balance

	def set_balance(self, b):
		self.balance = b

def transfer(a1, a2, x):
	a1_bal = a1.get_balance()
	if(a1_bal < x):
		print("not enough money")
	else:
		a2_bal = a2.get_balance()
		a1.set_balance(a1_bal - x)
		a2.set_balance(a2_bal + x)
		print("OK")