import random
num = random.randint(1, 9)
chances = 0
while(chances < 5):
    guess = int(input("Guess the number: "))
    chances = chances + 1
    if(guess == num):
        print("Congratulations, you won!")
        break
    elif(guess > num):
        print("Your guess was too high, guess again: ")
    else:
        print("Your guess was too low, guess again: ")
    #chances = chances + 1
if(not chances < 5):
    print("You lose! The number was ", num)