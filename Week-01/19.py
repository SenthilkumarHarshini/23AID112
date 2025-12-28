grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
count_A=0
count_B=0
count_C=0
count_D=0
for g in grades:
    if g>=90:
        count_A+=1
    elif g>=80:
        count_B+=1
    elif g>=70:
        count_C+=1
    else:
        count_D+=1
print("Number of students getting A:",count_A)
print("Number of students getting B:",count_B)
print("Number of students getting C:",count_C)
print("Number of students getting below 70:",count_D)