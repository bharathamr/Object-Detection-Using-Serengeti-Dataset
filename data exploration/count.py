f = open("animal.txt", "r")
arr = []

for x in f:
	if(x[:-1] == '' or x[:-1] == ' '):
		pass
	else:
		arr.append(x[:-1])

print(len(arr))
print(arr)
animal = []
for i in arr:
	if(i not in animal):
		animal.append(i)

print(len(animal))

found = []
l ={}

for j in arr: 
	if(j not in found):
		found.append(j)
		l[j] = 1
	else:
		l[j] +=1

print(l)
