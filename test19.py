a = [['Karen', 'Amanda'], ['Dan', 'Huck'], ['Tom', 'Bob']]
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])

for i in range(len(a)):
        for j in range(len(a[0])):
                print(a[i][j])

for i in a:
	print(i)
