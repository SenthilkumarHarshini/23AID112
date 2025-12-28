print("Enter a signal color: red, yellow or green")
signal=input()
if (signal=="red"):
    print("STOP!")
elif (signal=="yellow"):
    print("Prepare to stop.")
elif (signal=="green"):
    print("You can go.")
else:
    print("Wrong input.")