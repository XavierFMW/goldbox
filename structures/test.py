import chains

if __name__ == "__main__":

    struct = chains.Chain([x for x in range(10)])

    print(struct.head)
    print(struct.tail)

