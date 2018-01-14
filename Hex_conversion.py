import math

def conversion():
    address = input("Enter number. ")
    if address.isnumeric() == False:
        print ("Please enter a positive number")
        conversion()
    else:
        address = int(address)
    
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

    def hex_conversion(address):
        w = math.trunc(address / 4096)
        x = math.trunc((address % 4096) / 256)
        y = math.trunc((address % 256) / 16)
        z = (address % 16)
        if w != 0:
            print ("Your Hex number is: " + hex_ref[w], hex_ref[x], hex_ref[y], hex_ref[z], sep = "")
        elif w == 0:
            if x != 0:
                print ("Your Hex number is: " + hex_ref[x], hex_ref[y], hex_ref[z], sep = "")
            elif x == 0:
                if y != 0:
                    print ("Your Hex number is: " + hex_ref[y], hex_ref[z], sep = "")
                elif y == 0:
                    print ("Your Hex number is: " + hex_ref[z])
        again = input("Would you like to convert another number? ")
        again = again.lower()
        if again == "y" or again == "yes":
            conversion()
        else:
            print ("Goodbye.")
            exit()

    hex_conversion(address)

conversion()
    

