import random

yes = "y"
no = "n"
random_num_min = 1
roll_counter = 1
keep_playing = True

play = input("Welcome to diceroll!\nWould you like to roll a dice? y/n: ")

while play != yes and play != no:
    play = input("Please enter y or n!: ")

if play == yes:

    while keep_playing:
        sides = input("How many sides does your dice have? ")

        while not(sides.isdigit()):
            sides = input("Please enter a number: ")

        roll_count = input("How many times would you like to roll the dice? ")

        while not(roll_count.isdigit()):
            roll_count = input("Please enter a number: ")

        while roll_counter <= int(roll_count):
            print(random.randint(random_num_min, int(sides)))
            roll_counter += 1

        roll_counter = 1

        play_again = input("Would you like to roll another dice? y/n: ")

        while play_again != yes and play_again != no:
            play_again = input("Please enter y or n!: ")

        if play_again == no:
            keep_playing = False
            print("See you another day!")

elif play == no:
    print("See you another day!")