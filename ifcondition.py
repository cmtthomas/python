# if condition.py cmt

for j in range (0,10):
	print (j, " ",end="")
	if (j == 0):
		print(" Is Zero ")
	elif (j%2 == 0):
		print(" Is Even ")
	else:
		print("Is Odd ")
	print()
