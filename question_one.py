# This is a sample Python script.
import random
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Question_one:
    def __init__(self):
        pass
    def message_to_int(self, message = "Make Hong Kong great again"):
        cipher = [ord(char) - 96 for char in message]
        print(cipher)
        return cipher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    q_one = Question_one()
    q_one.message_to_int()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
