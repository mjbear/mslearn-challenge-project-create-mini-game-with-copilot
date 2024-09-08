import random


# https://learn.microsoft.com/en-us/training/modules/challenge-project-create-mini-game-with-copilot/4-exercise-create-the-game-logic
def play_game():
    global score, rounds_played  # Declare score and rounds_played as global variables
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        # return
        play_game()

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        score += 1  # Increment the score when the player wins
    else:
        print("Computer wins!")

    rounds_played += 1  # Increment the rounds_played variable

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print(f"Thank you for playing! Your score is: {score}")
        print(f"Total rounds played: {rounds_played}")

score = 0  # Initialize the score variable
rounds_played = 0  # Initialize the rounds_played variable
play_game()