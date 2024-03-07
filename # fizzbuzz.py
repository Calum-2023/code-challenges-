#fizzbuzz

target = 100

'''Create game fizzbuzz. if a selected number is divisable by 3 it outputs Fizz. if it is divisble by 5 it outputs Buzz. if it is 
divisible by both, it outputs FizzBuzz'''

for number in range(1,target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print ("FizzBuzz")
  elif number % 3 == 0:
    print ("Fizz")
  elif number % 5 == 0:
    print ("Buzz")
  else:
    print (number)