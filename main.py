x = y = 10

if (x < y):
  print("x is less than y")
else:
  if (x > y):
    print("x is greater than y")
  else:
    print("x and y must be equal")

# Exercise: Evaluate if your number is positive/negative/zero and odd/even.

num = int(input("Enter a number: "))

# positive
if (num > 0):
  print ("positive")

  if (num % 2 == 0):
    print ("Even number")
  
  else:
    print ("Odd number")

# negative
elif (num < 0):
  print ("negative")

  if (num % 2 == 0):
    print ("Even number")
  
  else:
    print ("Odd number")

# zero
else:
  print ("zero")