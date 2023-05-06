from random import choice
choices = ["Rock", "Paper", "Scissors"]
print("----------------------Welcome----------------------")
print("let's play some RPS!")
print("Be aware that if each of players  scores reaches to 5, Wins")
computer_score = 0
user_score = 0
while True:
    computer_input = choice(choices)
    if user_score == 5:
        print("you won! your scores reached to 5")
        play_again = input("do you want to play again?[yes/no]")
        if play_again.lower() == "no":
            break
        elif play_again.lower() != "yes":
            print("invalid value")
            break
        elif play_again.lower() == "yes":
            computer_score = 0
            user_score = 0
    elif computer_score == 5:
        print("you failed, computer score reached to 5")
        play_again = input("do you want to play again?[yes/no]")
        if play_again.lower() == "no":
            break
        elif play_again.lower() != "yes":
            print("invalid value")
            break
        elif play_again.lower() == "yes":
            computer_score = 0
            user_score = 0
    user_input = input("Enter Rock, Paper or Scissors: ")
    if user_input.title() not in choices:
        print("Invalid value error")
    elif user_input.title() == computer_input:
        print(f"Tie! Both of you choose the same {user_input}")
        print(f"your score: {user_score}\ncomputer score: {computer_score}")
    elif user_input.title() == "Rock":
        if computer_input == "Paper":
            print(f"oops you lose! computer chose {computer_input} and it beats {user_input}")
            computer_score += 1
            print(f"your score: {user_score}\ncomputer score: {computer_score}")
        else:
            print(f"you won! computer chose {computer_input} and {user_input} beats {computer_input}")
            user_score += 1
            print(f"your score: {user_score}\ncomputer score: {computer_score}")
    elif user_input.title() == "Paper":
        if computer_input == "Rock":
            print(f"you won! computer chose {computer_input} and {user_input} beats {computer_input}")
            user_score += 1
            print(f"your score: {user_score}\ncomputer score: {computer_score}")
        else:
            print(f"oops you lose! computer chose {computer_input} and it beats {user_input}")
            computer_score += 1
            print(f"your score: {user_score}\ncomputer score: {computer_score}")
    elif user_input.title() == "Scissors":
        if computer_input == "paper":
            print(f"you won! computer chose {computer_input} and {user_input} beats {computer_input}")
            user_score += 1
            print(f"your score: {user_score}\ncomputer score: {computer_score}")
        else:
            print(f"oops you lose! computer chose {computer_input} and it beats {user_input}")
            computer_score += 1
            print(f"your score: {user_score}\ncomputer score: {computer_score}")
