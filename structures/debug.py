import chains


if __name__ == "__main__":
    struct = chains.Deque([x for x in range(5)])
    struct.display_ends()
    print(struct)
