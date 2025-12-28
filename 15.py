given= [12, 45, 3, 98, 7, 34, 21]
for n in given:
    print (n)
print("Numbers greater than 30:")
count=0
for n in given:
    if n>30:
        print (n)
        count += 1
print("Count of numbers greater than 30 is",count)
