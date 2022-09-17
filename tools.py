
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

