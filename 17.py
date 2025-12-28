import random
numbers= random.sample(range(1,101),8)
biggest= numbers [0]
smallest= numbers [0]
for num in numbers:
    if num>biggest:
        biggest = num
    if num < smallest:
        smallest=num
print("List: ", numbers)
print("Biggest number: ", biggest)
print("Smallest number:", smallest)