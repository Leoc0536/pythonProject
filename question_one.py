# This is a sample Python script.
import random
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def question_one():
    # Use a breakpoint in the code line below to debug your script.
    message= "Make Hong Kong great again"
    for char in message:
        print(ord(char))

def question_four(x, y):
    n = 23
    g = 6
    # x = random.randint(1, 101)
    # y = random.randint(1, 101)

    print(f"{x = } \n{y = }")
    value = g**(x*y)%n
    print(f"{value = }")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question_one()
    question_four(2, 3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
