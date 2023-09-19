import random 
import math

# Taking Inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Lower bound:- "))

# generating random number between  
# the lower and upper 

x = random.randint(lower, upper)

print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      "chances to guess the integer!\n")

#initializing the number of guesses 
count = 0

# for calculation of minimun number of
# guesses depends upon range

while count < math.log(upper - lower + 1,2): 
  count +=1
  
  # Taking guessing number as input 
  guess = int(input("Guess a number :- "))
  
  #Coding testing 
  if x == guess:
    print("Congratulations you did it in ", 
          count, "try")
    
    # Once guessed, loop will break
    break
  elif x > guess:
    print("You guessed too small!")
  elif x < guess:
    print("You guessed too high!")
  
#If guessing is more than required guesses ,
# shows this output 
if count > math.log(upper - lower + 1, 2):
  print("\nThe number is %d" % x) 
  print("\tBetter Luck Next Time!") 
  