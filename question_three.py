import question_two
if __name__ == '__main__':
	q_two = question_two.Question_two()
	key = q_two.key_generator()
	q_two.encrypt_decrypt_test(key, "Hello World!")