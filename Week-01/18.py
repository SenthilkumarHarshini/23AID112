print("Number guessing game:Guess a number")
num=int(input())
while num != 7:
    if num>7:
        print("Too high")
    else:
        print("Too low")
    num=int(input("Try again:"))
print("Correct! You guessed it right")
    
