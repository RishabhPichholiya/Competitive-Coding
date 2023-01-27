n=int(input())
import math
def is_prime(n):
	if n <= 1:
		return False
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	for i in range(5, int(math.sqrt(n))+1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	return True
if(is_prime(n)):
    print(1)
elif(n%2==0):
    print(2)
elif(is_prime(n-2)):
    print(2) 
else:
    print(3)
