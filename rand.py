import random
import string


def randomValue(valueType):
    if type(valueType) is not dict:
        if valueType in basicTypes.keys():
            return basicTypes[valueType]()
    else:
        print(valueType)
        for key, value in valueType.items():
            print(key, " ", value)
            valueType[key] = randomValue(value)
        return valueType

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

basicTypes = {
        'int'   : rint,
        'bool'  : rbool,
        'string': rstring,
        'float' : rfloat,
        }
