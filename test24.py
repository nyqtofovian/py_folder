class Student:
	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.avg(30, 70)

#Surprisingly, on Python, you can create additional attributes like below, even after the statement of the class by each generated instances! 

a001.name = 'Sam'
print(a001.name)

