print("hi")
name = input("What's your name? ")

# remove whitespace from str and capitalize user's name using  methods 
# assignment operator to change value of variable  
name = name.strip().title() 

#split user input for name at a space to get first and last names individually
# first, last = name.split(" ")

print("hello, ", end="")
print(name)

print(f"hello, {name}")

# what we CAN pass to a function = parameter
# what we actually DO pass = argument 
# *objects = any number of objects
# [] usually mean optional

z = 1000000
print(f"{z:,}") #to format large number with commas to seperate by three digits

y = 200/3
print(f"{y:.2f}") #to round to two decimals


# FUNCTIONS 

def hello(username="world"): #world is the default value of the optional parameter username
    print(f"Hello {username}!")

hello() #call hello without any argument, so it prints Hello world!
name = input("Name: ")    
hello(name)


# ORGANIZATION
# def main() 
#   code that calls functions like hello() 
# def hello() and any other functions + their code
# call main() at the end

# SCOPE

variable = "global"

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return (n*n)

main()

# able to access a global variable in local functions, but cannot edit global var locally. 
# to be able to edit a global variable in a local function like main(), need to say "global varname" on the first line of main