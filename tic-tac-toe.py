"""
The Algorithm:
Take alternate inputs and keep the game on while
any of the 8 lists have a consistent consecutive value of
either a 0 or a 1. When they do the respective player wins
"""

co_ordinate = [[0, 1], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
co_ordinate_1 = [co_ordinate[0], co_ordinate[1], co_ordinate[2]]
co_ordinate_2 = [co_ordinate[3], co_ordinate[4], co_ordinate[5]]
co_ordinate_3 = [co_ordinate[6], co_ordinate[7], co_ordinate[8]]
co_ordinate_4 = [co_ordinate[0], co_ordinate[3], co_ordinate[6]]
co_ordinate_5 = [co_ordinate[1], co_ordinate[4], co_ordinate[7]]
co_ordinate_6 = [co_ordinate[2], co_ordinate[5], co_ordinate[8]]
co_ordinate_7 = [co_ordinate[0], co_ordinate[4], co_ordinate[8]]
co_ordinate_8 = [co_ordinate[2], co_ordinate[4], co_ordinate[6]]

co_ordinate_for_use = [co_ordinate_1, co_ordinate_2, co_ordinate_3, co_ordinate_4,
                       co_ordinate_5, co_ordinate_6, co_ordinate_7, co_ordinate_8]

positions = [i for i in range(9)]
new_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def user_input_one(value=0):
    position = int(input("Player 1: Enter position: "))
    if position in positions:
        return position, value


def user_input_two(value=1):
    position = int(input("Player 2: Enter position:: "))
    if position in positions:
        return position, value


def check_game():
    for i in co_ordinate_for_use:
        if i == [1, 1, 1]:
            return "2 wins"
        elif i == [0, 0, 0]:
            return "1 wins"


keep_going = True
while keep_going:
    user_input_one()
    user_input_two()
    check_game()
    if check_game():
        keep_going = False

