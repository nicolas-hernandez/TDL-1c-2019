import random
import string

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def rbool():
	valor = random.randint(0, 1)
	if valor == 1:
		return True
	else:
		return False

def rint():
    return random.randint(0, 999999999)

def rfloat():
    return round(random.uniform(0, 105), 1)

def rstring():
	chars = string.ascii_lowercase
	size = random.randint(0, 20)
	return random_string_generator(size, chars)

def randomI(typeI):
	#en typeI yo quiero que llegue el tipo del array
	if typeI == 'INT':
		return rint()
	if typeI == 'BOOL':
		return rbool()
	if typeI == 'FLOAT':
		return rfloat()
	if typeI == 'STR':
		return rstring()
		
		