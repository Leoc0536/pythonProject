class Question_one:
    def message_to_int(self, message = "Make Hong Kong great again"):
        cipher = [ord(char) for char in message]
        return cipher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message_in_int = Question_one().message_to_int()
    print(message_in_int)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
