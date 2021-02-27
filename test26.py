
class Student:
def __init__(self, name):
self.name = name

def calculate_avg(self, date):
sum = 0

for num in date:
sum += num

avg = sum / len(date)
return avg

def judge(self, avg):
if avg >= 60:
result = 'passed'
else:
result = 'faild'
return result

date_1 = [89, 42, 36, 95, 100, 4, 34]
a001 = Student('Gunillat')
avg = a001.calculate_avg(date_1)
result = a001.judge(avg)

print(avg)
print(a001.name + ' ' + result)