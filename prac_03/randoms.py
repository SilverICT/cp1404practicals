import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#What did you see on line 1?
#This print out a random integer between 5 and 20. like 5, 16, 27...
#What was the smallest number you could have seen, what was the largest?
#Smallest is 5, largest is 20.

#What did you see on line 2?
#This print out a random odd integer between 3 and 10. like 3, 5, 7...
#What was the smallest number you could have seen, what was the largest?
#Smallest is 3, largest is 9
#Could line 2 have produced a 4?
#No, it can only produce odd integer between 3 and 10.

#What did you see on line 3?
#This print out random floating-point numbers between 2.5 and 5.5, like 3.9628895, 5.23245535
#What was the smallest number you could have seen, what was the largest?
#Smallest is 2.5, Largest is infinite close to 5.5 but never equal to 5.5.

#Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

