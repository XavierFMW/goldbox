import random
import secrets


def get_random_int(start, end, inclusive=False, truly_random=False):
    if inclusive:
        end += 1

    if truly_random:
        return secrets.randbelow(end - start) + start

    else:
        return random.randrange(start, end)


def get_random_float(start, end, inclusive=False, truly_random=False):
    base = get_random_int(start * 100, end * 100, inclusive, truly_random)
    return base / 100
