class Save:
	def __init__(self, hp, ep):
		self.hp = hp
		self.ep = ep
	def message(self):
		print("HP : " + self.hp)

saved_data_1 = Save(99, 89)
saved_data_1.message()