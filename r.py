import random
r = random.randint(1,100)

while True:
	num = input("請猜數字1~100:")
	num = int(num)
	if num == r:
		print('答案正確')
		break
	elif num > r:
		print('你猜的數字比正確答案大喔')
		break
	elif num < r:
		print('你猜的數字比正確答案小喔')
		break
