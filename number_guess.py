import random
print('''Welcome to the Guess the Number game!
I'm thinking of a number between 1 and 100.''')
r=random.randint(1,100)
c=0
while True:
      g=int(input('Your guess: '))
      c+=1
      if g>r:
            print('Try a lower number')
      elif g<r:
            print('Try a higher number')
      else:
            break
print("Congratulations! You've guessed the number in",c,"attempts.")
print("Thanks for playing!")
