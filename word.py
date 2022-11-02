import random
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
with open("word.txt", "r") as file:
    allword = file.read()
    words = list(map(str, allword.split()))


def validity(word, char):
    for i in range(0, 5):
        if char == word[i]:
            return True
    return False


ran_word = random.choice(words)
ran_word = ran_word.lower()
# print(ran_word)
counter = 6
for i in range(1, counter):
    guess = input("\n Enter your word \n ")
    print(counter-i, "Chance left")
    # character checking or position checking
    for j in range(0, 5):
        # for x in guess:
        # if guess in ran_word:
        x = guess[j]
        if ran_word[j] == x:
            print(GREEN, x, RESET, "\t", end="")

        elif (validity(ran_word, x)):
            print(YELLOW, x, RESET, "\t", end="")

        else:
            print(RED, x, RESET, "\t", end="")

    # while(1):
        #     print("Correct match")
        #     break;
print("\n", ran_word)
