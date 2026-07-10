"""
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


def topings(cream):
    def top():
        
        print("cream added")
    return top

@topings
def icecream():
    print("choclate ice-cream")

print(icecream())
    


def colour(func):
    def warpar():
        return func().upper()
    return warpar


@colour
def colours():
    return "blue"

print(colours())
"""

def new_function(dare):
    def called():
        print("The file will be executing")
        print(dare())
        print("The file executing completed")
    return called  
 
    


@new_function
def function():
    return "Blue.txt"    

function()
