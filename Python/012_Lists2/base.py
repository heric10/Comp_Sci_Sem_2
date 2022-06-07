import random
a = int(input("How many random numbers do you want: "))
listt = []
for x in range(0,a):
    listt.append(random.randrange(1,10))
for x in range(0, a-1):
    print(listt[x], end=", ")
print(listt[a-1])
