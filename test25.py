
class Student:
        def __init__(self, name):
                self.name = name

        def avg(self, math, science, physics):
                return (math + science + physics) / 3

        def max_score(self, math, science, physics):
                if math > science and math > physics:
                        return math
                elif science > math and science > physics:
                        return science
                elif physics > math and physics > science:
                        return physics

a001 = Student('Gammo')
print(a001.name)
avg_result = a001.avg(40, 90, 80)

max_result = a001.max_score(40, 90, 80)

print(avg_result)
print(max_result)