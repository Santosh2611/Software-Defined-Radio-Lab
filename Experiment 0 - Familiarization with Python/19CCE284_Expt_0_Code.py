### Python Introduction
print("\nHello, World!") #Prints Hello, World!

### Python Lines and Indentation
if 5 > 2:
    print("Five is greater than two!\n")
    
### Python Comments    
#This is a comment
print("Hello, World!")
print("Hello, World!") #This is a comment
#print("Hello, World!")
print("Cheers, Mate!")
#This is a comment
#written in
#more than just one line
print("Hello, World!")
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!") 

### Python Variables
print("\n")    
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

# This will create two variables
a = 4
A = "Sally"
#A will not overwrite a

### Python Numbers
print("\n")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

### Python Assign Values to Multiple Variables
print("\n")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

### Python User Input
print("\n")
username = input("Enter username: ")
print("Username is: " + username)

### Python Collections (Arrays)
print("\n")
thislist = ["apple", "banana", "cherry"] 
print(thislist) # List

thistuple = ("apple", "banana", "cherry")
print(thistuple) # Tuple

thisset = {"apple", "banana", "cherry"}
print(thisset) # Set

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # Dictionaries

print("\n")
a = 33 # If
b = 200
if b > a:
  print("b is greater than a")

a = 33 # Elif
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
a = 200 # Else
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
a = 200 # And
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
a = 200 # Or
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
x = 41 # Nested If
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
a = 33 # The Pass Statement
b = 200
if b > a:
  pass

i = 1 # While Loop
while i < 6:
  print(i)
  i += 1

print("\n")
fruits = ["apple", "banana", "cherry"] 
for x in fruits: # For Loop
  print(x)

### Python Functions
print("\n")
def my_function1(): # Creating a Function
  print("Hello from a function!")
my_function1() # Calling a Function

def my_function2(fname): # Arguments
  print(fname + " Refsnes")
my_function2("Emil")
my_function2("Tobias")
my_function2("Linus") 

def my_function3(fname, lname): # Number of Arguments
  print(fname + " " + lname)
my_function3("Emil", "Refsnes") 

def my_function4(*kids): # Arbitrary Arguments, *args
  print("The youngest child is " + kids[2])
my_function4("Emil", "Tobias", "Linus")

def my_function5(child3, child2, child1): # Keyword Arguments
  print("The youngest child is " + child3)
my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function6(**kid): # Arbitrary Keyword Arguments, **kwargs
  print("His last name is " + kid["lname"])
my_function6(fname = "Tobias", lname = "Refsnes")

def my_function7(country = "Norway"): # Default Parameter Value
  print("I am from " + country)
my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

def my_function8(food): # Passing a List as an Argument
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function8(fruits)

def my_function9(x): # Return Values
  return 5 * x
print(my_function9(3))
print(my_function9(5))
print(my_function9(9)) 

### Python import Statements
print("\n")
import random
val1 = random.randrange(100);
val2 = random.randrange(100);
print("Following are the two generated random numbers under 100:-");
print("First: ",val1);
print("Second: ",val2);

### Python Classes/Objects
print("\n")
# Create a Class:-
# Create a class named MyClass, with a property named x
class MyClass:
  x = 5

# Create Object:-  
# Create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)

# The __init__() Function:-
# Create a class named Person, use the __init__() function to assign values for name and age
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age) 

# Object Methods:-
# Insert a function that prints a greeting, and execute it on the p1 object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello! My name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 

# The self Parameter:-
# Use the words mysillyobject and abc instead of self
class Person:
  def __init__(mysillyobject, name, age): 
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello! My name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 

# Modify Object Properties:-
p1.age = 40 # Set the age of p1 to 40

# Delete Object Properties:-
del p1.age # Delete the age property from the p1 object

# Delete Objects:-
del p1 # Delete the p1 object

# The pass Statement:-
class Person:
  pass

### Python Libraries
print("\n")
import numpy as np # Support for large, multi-dimensional arrays and matrices
import matplotlib.pyplot as plt # Provides an implicit way of plotting

x = np.ones(10) # Returns a new array of given shape and type, with ones

plt.subplot(121) # subplot(rows, columns, index) describes the figure layout
plt.plot(x) # Used to draw points (markers) in a diagram, draws a line from point to point
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Continuous unit step')

plt.subplot(122) # subplot(rows, columns, index) describes the figure layout
plt.stem(x) # Stem plot plots vertical lines at each x position covered under the graph from the baseline to y, and places a marker there.
plt.xlabel('n index')
plt.ylabel('Amplitude')
plt.title('Discrete unit step')
