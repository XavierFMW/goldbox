import misc


if __name__ == "__main__":
    struct = misc.RangeDict()
    struct.set(10, 20)
    struct.set(20, 30)
    struct.set(30, 40)

    print(struct)
