''' 
Find the factors of an interger
'''
#find-factors.py CMT

def factors(b):
	for i in range(1, b+1):
		if b % i == 0:
			print(i)
if __name__ == '__main__' :
	b = input('Your number please: ' )
	b = float(b)
	
	if b> 0 and b.is_integer():
		factors(int(b))
	else:
		print('please enter a positive integer')

