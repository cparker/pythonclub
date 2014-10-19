# Simple if/else example

while True:
  food = input('what is your favorite food? ')

  # only ONE of these cases will match
  if (food == 'banana'):
    print("Don't slip on the peel\n")
  elif (food == 'apple'):
    print("They say an apple a day keeps the doc away\n")
  elif (food == 'orange'):
    print("Oranges have lots of vitamin C\n")
  elif (food == 'bye'):
    print("Bye!\n")
    exit()
  # this is the 'default' case.  This runs if nothing above matches
  else:
    print("I don't know anything about that fruit\n")
