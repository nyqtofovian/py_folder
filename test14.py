class Save:
	def __init__(self, hp, ep, lv):
		self.hp = hp
		self.ep = ep
		self.lv = lv
	def notification(self):
		print('HP : ' + self.hp)
		print('EP : ' + self.ep)
		print('Lv : ' + self.lv)

lv_a = 23
ep_a = 12
hp_a = 2

lv_b = 99
ep_b = 999
hp_b = 999

save_data_a = Save(hp_a, ep_a, lv_a)
save_data_b = Save(hp_b, ep_b, lv_b)

print(save_data_a.notification())
print(save_data_b.notification())