num = [6,9,32,28,15,22,3,18]

minimum = num[0]
for i in num:
    if i<minimum:
        minimum=i
print("Minimum")
print(minimum)
print("")

maximum = num[0]
for i in num:
    if i>maximum:
        maximum=i
print("Maximum")
print(maximum)
print("")

average=0
count=0
for i in num:
    average=average+i
    count=count+1
average = average/count
print("Average")
print(average)