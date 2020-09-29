"""
Author: Derek Bittner
Program: validate_input_in_functions.py

prompts user for name and score, prints values to console.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):


    """

    :param test_name:
    :param test_score:
    :param invalid_message:
    :return:
    """

    # print("{}: {}".format(test_name, test_score))
    return "{}: {}".format(test_name, test_score)


if __name__ == '__main__':
    score_input("test1, 45")
