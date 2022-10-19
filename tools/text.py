
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
