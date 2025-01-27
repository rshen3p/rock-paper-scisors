import random


# get the input from the user
# determine if input is valid, if not then keep asking
def get_user_input():
    user_input = input("Please choose your move: 'r' for rock, 'p' for paper, 's' for scissor: ")
    if user_input == 'r' or user_input == 'p' or user_input == 's':
        return user_input
    else:
        print("\nYou have entered an invalid input, please enter a valid move: r - rock, p - paper, s - scissor\n")
        user_input = "invalid"
        return user_input


# get the input from the computer
def computer_choice():
    command_list = ['p', 'r', 's']
    index = random.randint(0, 2)
    return command_list[index]


# convert short input to full input for better reading
def convert_input(input_move):
    full_input = ''
    if input_move == 's':
        full_input = 'scissor'
    elif input_move == 'r':
        full_input = 'rock'
    elif input_move == 'p':
        full_input = 'paper'
    return full_input


# explain to user why the loss
def print_lose_msg(user_input, computer_input):
    print(f'\nUser has LOST! Computer used {computer_input} to beat {user_input}\n')


# explain to user why the win
def print_win_msg(user_input, computer_input):
    print(f'\nUser has WON! User used {user_input} to beat {computer_input}\n')


# logic to determine the outcome of the game
def compare_input(user_input, computer_input):
    user_input = convert_input(user_input)
    computer_input = convert_input(computer_input)

    if user_input == computer_input:
        print(f"\nBoth user and the computer chose {user_input}, so this round is a tie!\n")
    elif user_input == 'rock':
        if computer_input == 'paper':
            print_lose_msg(user_input, computer_input)
        else:
            print_win_msg(user_input, computer_input)
    elif user_input == 'paper':
        if computer_input == 'scissor':
            print_lose_msg(user_input, computer_input)
        else:
            print_win_msg(user_input, computer_input)
    elif user_input == 'scissor':
        if computer_input == 'rock':
            print_lose_msg(user_input, computer_input)
        else:
            print_win_msg(user_input, computer_input)


# determine if user still wants to continue playing
def is_continue():
    user_input = input("Please enter 'y' if want to continue playing, other wise enter 'n' to quit: ")
    if user_input == 'y':
        print("\nLet's play again!\n")
        return True
    elif user_input == 'n':
        print("\nThanks for playing, bye!\n")
        return False
    else:
        print("\nInvalid input, terminating program!\n")
        return False


# the driver function for the program
def main():
    print("Welcome to the Rock-Paper-Scissor game!")
    while True:
        user_input = get_user_input()
        if user_input == "invalid":
            continue
        computer_input = computer_choice()
        compare_input(user_input, computer_input)
        if not is_continue():
            exit()


if __name__ == "__main__":
    # execute only if run as a script
    main()
