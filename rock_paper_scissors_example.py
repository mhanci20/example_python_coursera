#!/usr/bin/env python3

import random

def play():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors,or q to quit): ").lower()

        if user_choice == 'q':
            break

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
play()
