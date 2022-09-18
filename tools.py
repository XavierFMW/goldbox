import random
import secrets

def file_to_list(filename):

    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines() if line != ""]
        return lines


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

