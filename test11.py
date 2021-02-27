
class Card:
        def __init__(self, date, user_name):
                self.date = date
                self.user_name = user_name
        def message(self):
                return 'This comment is uploaded by ' + self.user_name + ' on ' + self.date
date_a = '2021-02-13'
user_name_a = 'Tyson'
card_a = Card(date_a, user_name_a)

date_b = '2020-01-03'
user_name_b = 'Karen'
card_b = Card(date_b, user_name_b)

print(card_a.message())
print(card_b.message())