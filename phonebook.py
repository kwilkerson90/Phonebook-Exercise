#PRACTICING WORKING THROUGH THE PHONE BOOK APP




print("ELECTRONIC PHONE BOOK") 
print("1. Look up an entry")
print("2. Set an entry")
print("3. Delete an entry")
print("4. List all entries")
print("5. Quit")
print("How can I help you?")

person = {
    "first": "Kendra",
    "second": "Kru",
    "third": "Dominique"
}
number = {
    "first": "111-111-1111",
    "second": "222-222-2222",
    "third": "333-333-3333"
}
#THIS BLOCK OF CODE WILL ALLOW THE USER TO SET/SAVE A NEW CONTACT
def entries():
    names = ["Kendra", "Kru", "Dominique"]
    
    print ("Would you like to add?")
    a = input()
    if a == ("yes"):
        b = input()
entries()

def contactinfo():
    numbers = ["111", "222", "333"]

    print ("Would you like to add?")
    a = input()
    if a == ("yes"):
        b = input()
contactinfo()

