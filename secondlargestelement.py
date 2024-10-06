Length=int(input())
Array=[]
for i in range(Length):
    integers=int(input())
    Array.append(integers)
First_largest=0
Second_largest=0
for i in Array:
    if i>First_largest:
        Second_largest=First_largest
        First_largest=i
    elif i > Second_largest and i != First_largest:
        Second_largest = i
print("The Second Largest element is:",Second_largest)
