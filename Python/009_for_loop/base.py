l = int(input("How long should your line be? "))
s = input("Should your line be Vertical or Horizontal? ")
if s == "Vertical":
    for x in range(0,l):
        print("*")
if s == "Horizontal":
    for x in range(0,l):
        print("*", end="")