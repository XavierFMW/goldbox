import chains


if __name__ == "__main__":
    first = chains.Stack([x for x in range(5)])
    second = chains.Chain([x for x in range(5)])
    print(first >= second)
