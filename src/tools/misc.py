import time


def time_it(function):

	def wrapper(*args, **kwargs):
		start = time.time()
		response = function(*args, **kwargs)
		end = time.time()

		difference = end - start
		print(f"{function.__name__}: {round(difference * 1000)}")
		return response

	return wrapper
