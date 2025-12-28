print("Enter temperature in celsius:")
Ctemp=int(input())
Ftemp=Ctemp*(9/5)+32
if (Ftemp<0):
    print("Very cold! Wear thick jacket.")
elif (Ftemp<=15):
    print("Cold. Wear Jacket.")
elif (Ftemp<=25):
    print("Nice weather.")
else:
    print("Hot! Stay hydrated")
