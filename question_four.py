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

    question_four(2, 3)