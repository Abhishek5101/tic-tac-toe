"""
The Algorithm:
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


def user_input_one():
    x = int(input("X-co_ordinate: "))
    y = int(input("Y-co_ordinate: "))
    if [x, y] in co_ordinate:
        return [x, y], 0


def user_input_two():
    x = int(input("X-co_ordinate: "))
    y = int(input("Y-co_ordinate: "))
    if [x, y] in co_ordinate:
        return [x, y], 1

#
# keep_going = True
# while keep_going:
#     user_input_one()


