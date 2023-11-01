import sympy
import random
import math
import question_one
import question_two_three

class Question_two:
	def question_two(self):

		q_one = question_one.Question_one()
		prime_number = list(sympy.primerange(1, 100))

		print(prime_number)
		p, q = random.choices(prime_number, k=2)
		print(f"{p = }\n{q = }")

		n = p*q
		z = (p-1) * (q-1)
		e_list = []
		i=0
		while i < 10:
			temp = random.randint(2, n-1)
			if math.gcd(z, temp) == 1:
				e_list.append(temp)
				i+=1
		print(f"{e_list = }")
		e = min(e_list)
		d = None
		for i in range(100_000_000):
			if (i*e-1)%z == 0:
				d = i
				if d==e:continue
				break

		print(f"{z = }")
		print(f"{e = }")
		print(f"{d = }")


		message = q_one.message_to_int("hello")


		encrypt = [m**e%n for m in message]
		print(f"{encrypt = }")

		decrypt = list(map(lambda x: pow(x, d) %n , encrypt))
		print(f"{decrypt = }")

		from PIL import Image
		im = Image.open("big_5b252c1a32b7d.jpg")
		# im.show()
		print(f"{im.width = }")
		print(f"{im.height = }")
		px = im.load()
		print(px[0,0])
		for x in range(im.width):
			for y in range(im.height):
				pix = px[x, y]
				encrypt_photo = pow(pix, e)%n
				px[x, y] = encrypt_photo

		im.show()



if __name__ == '__main__':
	q_two = question_two_three.Question_two()
	q_two.question_two()