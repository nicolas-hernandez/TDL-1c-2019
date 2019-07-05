import random
import string
from copy import deepcopy


def randomValue(valueType):
    if type(valueType) is not dict:
        if valueType in basicTypes.keys():
            return basicTypes[valueType]()
    else:
        for key, value in valueType.items():
            if key == '[]':
                tam = random.randint(0, 10)
                array = []
                for x in range(tam):
                    arrayType = deepcopy(value)
                    array.append(randomValue(arrayType))
                return array
            valueType[key] = deepcopy(randomValue(value))
        return deepcopy(valueType)


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

basicTypes = {
        'int'   : rint,
        'bool'  : rbool,
        'string': rstring,
        'float' : rfloat,
        }
