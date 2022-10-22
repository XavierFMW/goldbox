import trees


if __name__ == "__main__":
    struct = trees.BinaryTree([x for x in range(7)])

    struct.pop(2)
    print(struct.index(0))
    print(struct.index(1))
    print(struct.index(2))
    print(struct.index(3))
    print(struct.index(4))
    print(struct.index(5))
    print(struct.index(6))
