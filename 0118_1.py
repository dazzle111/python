#coding = utf-8
#!/usr/bin/python

class worker:
	def __init__(self,name,pay):
		self.name = name
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay *= (1.0+percent)

bob = worker('bob smith',50000)
sue = worker('sue jones',60000)
print 'bob lastname',bob.lastName()
print 'sue lastname',sue.lastName()
print 'sue raise',sue.giveRaise(.10)
print 'sue pay',sue.pay
