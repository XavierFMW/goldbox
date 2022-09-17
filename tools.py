
def file_to_list(filename):

    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines() if line != ""]
        return lines
