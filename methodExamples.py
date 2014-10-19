# a method with no arguments

def printChristiansName():
  print("Christian")

def printAnyName(theName = "Chris"):
  print(theName)

# this method takes three parameters and returns a value
def addThreeNumbers(first,second,third):
  return first + second + third
  


printChristiansName()
printAnyName("fred")
printAnyName(theName="fred")
printAnyName()

print ( addThreeNumbers(1,2,3) )
print ( addThreeNumbers(first=1,second=2,third=3) )


