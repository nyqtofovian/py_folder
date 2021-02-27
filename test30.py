
class Person:
        def __init__(self, name, nationality, age):
                self.name = name
                self.nationality = nationality
                self.age = age

        def __call__(self):
                print('This is a call-fucntion!')

        def say_hello(self, name):
                print('Hi {0}! Im {1}.'.format(name, self.name))

kenta = Person('Kenta', 'Japan', 27)
kenta.say_hello('Pixy Flog')
kenta()
