import sympy
import random

def question_two():
	prime_number = list(sympy.primerange(1, 100))

	print(prime_number)
	p, q = random.choices(prime_number, k=2)
	print(f"{p = }\n{q = }")





if __name__ == '__main__':
	question_two()