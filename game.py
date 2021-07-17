import random


# get the input from the user
# determine if input is valid, if not then keep asking
def get_user_input():
    user_input = input("Please choose your move: 'r' for rock, 'p' for paper, 's' for scissor: ")
    if user_input == 'r' or user_input == 'p' or user_input == 's':
        return user_input
    else:
        print("Your choice " + user_input +
              " is an invalid input, please enter a valid move: r - rock, p - paper, s - scissor")
        get_user_input()


# get the input from the computer
def computer_choice():
    command_list = ['p', 'r', 's']
    index = random.randint(0, 3)
    return command_list[index]


# the driver function for the program
def main():
    print("Welcome to the Rock-Paper-Scissor game!")
    user_input = get_user_input()
    print("User chose: " + user_input)
    computer_input = computer_choice()
    print("Computer chose: " + computer_input)


main()
