from time import sleep
sleep(50.0) # sleep 50.0 seconds

class vector:
	def __init__(self, x):
		self.x = x
	
	def check(self, b):
		if len(self.x) == len(b.x):
			print("True")
		else:
			print("Fatal error")
	
	def __add__(self, b):
		c = vector(range(len(self.x)))
		for i in range(len(self.x)):
			c.x[i] = self.x[i] + b.x[i]
		return c

	def __sub__(self, b):
		c = vector(range(len(self.x)))
		for i in range(len(self.x)):
			c.x[i] = self.x[i] - b.x[i]
		return c
	
	def scal_mul(self, b):
		p = 0
		for i in range(len(self.x)):
			p = p + self.x[i] * b.x[i]
		return p
		



x1 = [1,2,3]
x2 = [0,0,1]		
a = vector(x1)
b = vector(x2)
c =  a + b
print c
c = a - b
print c
c = a.scal_mul(b)
print c