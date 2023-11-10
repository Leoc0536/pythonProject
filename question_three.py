import question_two
from PIL import Image
def encrypt_image(key):
	im = Image.open("big_5b252c1a32b7d.jpg")
	px = im.load()
	print(key)
	n, encrypt_key = key["encrypt"]
	
	enc = [[0 for x in range(im.height)] for y in range(im.width)]
	for x in range(im.width):
		for y in range(im.height):
			enc[x][y] = pow(px[x, y], encrypt_key, n)
			px[x, y] = enc[x][y]%256
	im.save("Encrypted.jpg")

	n, decrypt_key = key["decrypt"]
	for x in range(im.width):
		for y in range(im.height):
			px[x, y] = pow(enc[x][y], decrypt_key, n)
	im.save("Decrypted.jpg")
	
	
if __name__ == '__main__':
	q_two = question_two.Question_two()
	key = q_two.key_generator()
	encrypt_image(key)