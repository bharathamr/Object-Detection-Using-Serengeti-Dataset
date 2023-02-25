import os
s = "/home/bhuvanaj/yolov5/yolov5/data/custom_image/"
arr = ['Hippopotamus', 'GuineaFowl', 'Aardvark', 'Aardwolf']
b = 3
a = os.listdir(s+arr[b])
a.sort()
for i in a:
	if ".txt" not in i:
		pass
	else:
		f = open(s+arr[b]+"/"+i,"r")
		s1 = f.readline()
		m = s1.split(" ")
		m[0] = '3'
		s1 = m[0]+" "+m[1]+" "+m[2]+" "+m[3]+" "+m[4]
		print(s1)
		f.close()
		f = open(s+arr[b]+"/"+i,"w")
		f.write(s1)
		f.close

