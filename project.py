# The number guessing game
import random

print("WELCOME TO THE NUMBER GUESSING GAME")
print("AM THINKING OF A NUMBER BETWEEN 1 AND 100")
number = random.randint(1, 101)
print(number)
difficulty = input("Choose difficulty, type 'easy' or 'hard': ").lower()
number_of_attempts = 0
if difficulty == 'easy':
    number_of_attempts = 10
    print(f"You have {number_of_attempts} remaining to guess the number")
elif difficulty == 'hard':
    number_of_attempts = 5
    print(f"You have {number_of_attempts} remaining to guess the number.")

guess = int(input("Make a guess: "))
game_continuing = True
while game_continuing:
    if guess > number:
        print("Too high")
        number_of_attempts -= 1
        if number_of_attempts == 0:
            print(f"You went out of attempt, the number was {number}")
            game_continuing = False
        else:
            guess = int(input("Guess again: "))
    elif guess < number:
        print("Too low")
        number_of_attempts -= 1
        if number_of_attempts == 0:
            print(f"You went out of attempt, the number was {number}")
            game_continuing = False
        else:
            guess = int(input("Guess again: "))
    elif guess == number:
        print(f"You win The number was {number}, Your score is {number_of_attempts}")
        game_continuing = False
