import sympy
import random
import math
import question_one

class Question_two:
	def __init__(self):
		self.q_one = question_one.Question_one()

	def key_generator(self, p=5, q=51):
		prime_number = list(sympy.primerange(17, 100))

		p = random.choice(prime_number)
		prime_number.remove(p)
		# ensure distinct p, q
		q = random.choice(prime_number)
		print(f"{p = }\t{q = }")

		n = p * q
		z = (p-1) * (q-1)
		e_list = []
		for temp in list(sympy.primerange(2, n)):
			if math.gcd(z, temp) == 1:
				e_list.append(temp)

		e = min(e_list)
		d = None

		# find the smallest value of d that satisfy ed-1 % n = 0
		for d in range(100_000):
			if not d == e :
				if (d * e - 1) % z == 0:
					break
		return {"encrypt": (n, e), "decrypt": (n, d)}

	def encrypt_decrypt_test(self, key, message="hello"):
		print(f"Message to encrypt: {message}\n")

		# get key
		n, encrypt_key = key["encrypt"]
		n, decrypt_key = key["decrypt"]

		# convert to unicode
		message_to_int = self.q_one.message_to_int(message=message)

		# start encryption
		encrypt = [pow(m, encrypt_key) % n for m in message_to_int]
		encrypt_str = "".join([chr(e) for e in encrypt])
		print(f"Message after encryption in int: {encrypt}")
		print(f"Message after encryption: {encrypt_str}\n")

		# start decryption
		decrypt = [pow(c, decrypt_key) % n for c in encrypt]
		decrypt_str = "".join([chr(d) for d in decrypt])
		print(f"Message after decryption in int: {decrypt}")
		print(f"Message after decryption: {decrypt_str}")


if __name__ == '__main__':
	q_two = Question_two()
	key = q_two.key_generator()
	q_two.encrypt_decrypt_test(key)


