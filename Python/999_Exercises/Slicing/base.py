name = input(str("What is your first and last name? "))

for nam in range(0,len(name)):
    y = name[nam:nam+1]
    print(y)
    
for space in range(0,len(name)):
    y=name[space:space+1]
    x=" "
    if y==x:
        name1=name[space:len(name)]
        name2=name[0:space]
        print(name1 + ", " + name2)