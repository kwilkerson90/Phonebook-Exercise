#PRACTICING WORKING THROUGH THE PHONE BOOK APP







print("ELECTRONIC PHONE BOOK") 
print("1. Look up an entry")
print("2. Set an entry")
print("3. Delete an entry")
print("4. List all entries")
print("5. Quit")
print("How can I help you?")


name = {
    "name1": "Kendra",
    "name2": "Kru",
    "name3": "Dominique"
}
number = {
    "num1": "111",
    "num2": "222",
    "num3": "333"
}

#THIS BLOCK OF CODE WILL ALLOW THE USER TO LOOK UP THE CORRESPONDING NUMBER FOR A GIVEN NAME 
name = input("Enter name:")
#a = number.get("num2")
#print(a)
x = number.get("num1")
if name == "Kendra":
    print(x)

y = number.get("num2")
if name == "Kru":
    print(y)

z = number.get("num3")
if name == "Dominique":
    print(z)



"""
name1 = "Kendra"
name2 = "Kru"
name3 = "Dominique"

number1 = "111"
number2 = "222"
number3 = "333"
"""
















#THIS BLOCK OF CODE WILL ALLOW THE USER TO SET/SAVE A NEW CONTACT

def entries():
    names = ["Kendra", "Kru", "Dominique"]
    
    #print ("Would you like to add?")
    a = input("Would you like to add?")
    if (a == "yes"):
        b = input("What's your name?")
        names.append(b)
        print(names)
entries()

def contactinfo():
    numbers = ["111", "222", "333"]

    #print ("Would you like to add?")
    a = input("Can I have your number?")
    if (a == "yes"):
        b = input("What's your number?")
        numbers.append(b)
        print(numbers)
contactinfo()
    #elif ()


