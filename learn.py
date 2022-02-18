# SCOPE IN PYTHON

# namespace: local vs global scope in python
enemies = 1
def increase_enemies():
    global enemies #defining a global variable
    enemies = 2
    print(f"enemies inside the function: {enemies}.")
increase_enemies() #enemies inside the function: 2
print(f"Enemies outside the function: {enemies}.") #1 enemies

#local scope
# exists within functions
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
#print(potion_strength)#NameError: name 'potion_strength' is not defined
# functions created inside a function can only be used inside that function

# Global scope
player_health = 10
def drink_potion2():
    potion_strength = 2
    print(player_health)
drink_potion2() # 10
# the concept of global and local scope does not only apply to variables, it also applies to anything else we name eg functions inside functions, dictionaries,lists etc


# There is NO BLOCK SCOPE IN PYTHON: which means that any variable inside a block of code eg if statement, while loop etc can be used globally.

# Global constants: values that never change in our code eg the value of pi
# in python, to differentiate constants to variables, we write the constants in uppercase
PI = 3.142
URL = "https://www.google.com"