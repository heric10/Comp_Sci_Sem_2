people_list = ["Mom", "Dad", "Brother", "Friend"]
comp_list = ["is smart.", "has a great personality.", "is good at Among Us.", "rocks!"]

import random
peoplnum = random.randrange(0,len(people_list))
compnum = random.randrange(0,len(comp_list))

print(people_list[people_num] + " " + comp_list[compnum])
