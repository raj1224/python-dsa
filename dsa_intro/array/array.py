# FOR LOOP
for i in range(0,6):
    print(i)

print('\n')

# ENHANCED FOR LOOP
val = [1,2,3,4,5]
for i in val:
    print(i)

# REVERSE
val.reverse()
print('\n')
for i in val:
    print(i)

# insert
val.insert(2, 10)
val.append(20)
val.pop()
val.pop("index")
val.remove(10)

# length
len(val)

# range
for i in range(len(val)):
    print(val[i])

# new array with older array
abc = val["start":"end"]

# slicing
abc = val[::-1]

# input
n = int(input("Enter the number of elements: "))

# index
arr = [1,2,3,4,5,10]
i = arr.index(10)
