import random

myArr = [2, 3, 4, 1, 2]
print(myArr)

# [2, 3, 4, 1, 2]
#           ^
#           \

myArr[3] = 3
print(myArr)

myArr.append(20)
print(myArr)

print(len(myArr))

print(random.randint(0, len(myArr) - 1))