def keygen(x, r,size):
	key=[]
	for i in range(size):
		x=r*x*(1-x)
		key.append(int((x* pow(10,16))%100))

     
	return key

key = keygen(0.01,3.95,10)
print(key)