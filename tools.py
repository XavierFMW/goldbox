import random
import secrets


def get_lines(filename, collapse_whitespace=True):

	with open(filename, "r") as file:

		if collapse_whitespace:
			return [line.strip() for line in file.readlines() if line != ""]
		else:
			return [line + "\n" for line in file.read().split("\n")]


def replace_text_in_file(filename, old, new):
	
	lines = get_lines(filename, False)

	with open(filename, "w") as file:
		for line in lines:
			file.write(line.replace(old, new))


def shrink(filename, spaces=4):
	replace_text_in_file(filename, old=(" " * spaces), new="\t")


def grow(filename, spaces=4):
	replace_text_in_file(filename, old="\t", new=(" " * spaces))


def timeit(function):

	def wrapper(*args, **kwargs):
		start = time.time()
		response = function(*args, **kwargs)
		end = time.time()

		difference = end - start
		print(f"{function.__name__}: {round(difference * 1000)}")
		return response

	return wrapper


def get_random_int(start, end, inclusive=False, truly_random=False):

	if inclusive:
		end += 1

	if truly_random:
		return secrets.randbelow(end - start) + start

	else:
		return random.randrange(start, end)


def get_random_float(start, end, inclusive=False, truly_random=False):
	base = get_random_int(start*100, end*100, inclusive, truly_random)
	return base / 100


