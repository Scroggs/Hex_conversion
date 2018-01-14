import math    
hex_ref = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f"
    }
def play_again():
    again = input("Would you like to convert another number? y/n ")
    again = again.lower()
    if again == "y" or again == "yes" or again == "":
        conversion()
    elif again == "n" or again == "no":
        print ("Dilly Dilly, goodbye.")
        exit()
    else:
        print ('Please choose "y" or "n" ')
        play_again()

def hex_conversion(address):
    hex_number = []
    if address == 0:
        print ("Your hex number is: 0")
        play_again()
    else:
        while address != 0:
            x = math.trunc(address % 16)
            hex_number.append(hex_ref[x])
            address = math.trunc(address / 16)
    print ("Your hex number is: " + "".join(reversed(hex_number)))
    play_again()

def conversion():
    address = input("Enter a number: ")
    if address.isnumeric() == False:
        print ("Please enter a positive number")
        conversion()
    else:
        address = int(address)
    hex_conversion(address)

conversion()




  
