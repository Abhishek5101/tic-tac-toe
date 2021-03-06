"""
The Algorithm:
Take alternate inputs and keep the game on while
any of the 8 lists have a consistent consecutive value of
either a 0 or a 1. When they do the respective player wins
"""

co_ordinate = [7, 7, 7, 7, 7, 7, 7, 7, 7]


def user_input_one():
    position = int(input("Player 1: Enter position: "))
    # co_ordinate.insert(position, 0)
    return position


def user_input_two():
    position = int(input("Player 2: Enter position: "))
    # co_ordinate.insert(position, 1)
    return position


co_ordinate_1 = [co_ordinate[0], co_ordinate[1], co_ordinate[2]]
co_ordinate_2 = [co_ordinate[3], co_ordinate[4], co_ordinate[5]]
co_ordinate_3 = [co_ordinate[6], co_ordinate[7], co_ordinate[8]]
co_ordinate_4 = [co_ordinate[0], co_ordinate[3], co_ordinate[6]]
co_ordinate_5 = [co_ordinate[1], co_ordinate[4], co_ordinate[7]]
co_ordinate_6 = [co_ordinate[2], co_ordinate[5], co_ordinate[8]]
co_ordinate_7 = [co_ordinate[0], co_ordinate[4], co_ordinate[8]]
co_ordinate_8 = [co_ordinate[2], co_ordinate[4], co_ordinate[6]]


co_ordinate_to_check = [co_ordinate_1, co_ordinate_2, co_ordinate_3, co_ordinate_4,
                        co_ordinate_5, co_ordinate_6, co_ordinate_7, co_ordinate_8]


def game_over():
    for i in co_ordinate_to_check:
        if i == [1, 1, 1]:
            print("2 wins")
        elif i == [0, 0, 0]:
            print("1 wins")


keepgoing = True
while keepgoing:
    position = user_input_one()
    co_ordinate[position] = 0
    print(co_ordinate)
    if game_over():
        keepgoing = False
    position2 = user_input_two()
    co_ordinate[position2] = 1
    print(co_ordinate)
    if game_over():
        keepgoing = False

