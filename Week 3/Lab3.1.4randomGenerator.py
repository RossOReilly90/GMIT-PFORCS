#
# program that prints out a random number between 1 and 10
#

import random

num1 = int(input("Please enter an interger: "))
num2 = int(input("Please enter an another interger: "))

randomNum = random.randint(min(num1, num2),max(num1,num2))	# min & max used to ensure first param < second param
print ("Today's random number {}" .format(randomNum))