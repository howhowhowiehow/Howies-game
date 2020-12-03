import time

def GoToGameStop():
    print ("Howie keeps walking down the street, and sees game stop.")
    goInside = input("Should he go inside? ")

    if goInside == "yes":
        print()
        print("Howie goes into game stop. He goes into the mario section. Howie finds 100,000 dollars on the floor.")
        
letsPlay = input("Hello. Would you like to play the game? ")

if letsPlay == "yes" or letsPlay == "sure" or letsPlay == "okay":
    
    print()
    print("OK, let's play.")

    print()
    print("One day Howie was walking down the street.")
    print("He saw a spooky house.")
    goInside = input("Should he go inside? ")

    print()
    
    if goInside == "yes":
        print ("Howie walks inside the house, and finds a ghost. The ghost is spooky.")
        adventuring = input("Do you think Howie should keep on adventuring through? ")
        if adventuring == "yes":
             print ("Howie is scared.")

    else:
        GoToGameStop()
   
else:
    print("OK, goodbye.")

time.sleep(4)

