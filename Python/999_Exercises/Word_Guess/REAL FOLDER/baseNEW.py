import random
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)
print(word_list)

num = random.randrange(12972)
answer = word_list[num]
print(answer)

a = 0
for i in range(0,6):
    guess = input("Guess a word! ")
    if guess == answer:
        print("You won!")
        a = 1
        break
    else:
        print("Guess again...")
if a == 0:
    print("You lost! The word was: "+ answer)