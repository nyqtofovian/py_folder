mr_a = 25
ms_b = 12

if mr_a >= 20:
	print('adult')
elif mr_a < 20 and mr_a > 2:
	print('child')
else:
	print('baby')

for i in range(20):
	if i == ms_b:
		continue
	print(i)