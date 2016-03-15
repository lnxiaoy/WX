import random
total = 50
num = 9
min = 0.01
for i in range(1,num,1):
	safe = (total-(num-i)*min)/(num-i)
	money = float(random.randint(int(min*100),int(safe*100)))/100
	total = total-money
	print ("第%d个红包，金额为%.2f，余额为%.2f" %(i,money,total))
print ("第%d个红包，金额为%.2f，余额为0.00" %(num,total))