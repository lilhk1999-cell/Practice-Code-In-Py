import random
lowest_num=1
highest_num=100
answer= random.randint(lowest_num,highest_num)
guesses=0
is_running= True

print("==GUESSING GAME==")
print(f"Choose a number between {lowest_num} and {highest_num} ")

while is_running:
    guess= input("Entre your guess: ")
    print()
    if guess.isdigit():
        guess= int(guess)
        guesses +=1
        if guess < lowest_num or guess > highest_num:
            print("Your guess is out of range!")
            print(f"Please choose a number between {lowest_num} and {highest_num} ")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! the answer was {answer}")
            print(f"Number of guesses {guesses}")
            is_running = False
    else:
        print("INVALIDE GUESS")
        print(f"Please choose a number between {lowest_num} and {highest_num} ")