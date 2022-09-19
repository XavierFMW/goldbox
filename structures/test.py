import chains

if __name__ == "__main__":
    
	arr = [x for x in range(10)]
	struct = chains.Queue(arr)

	for x in struct:
		print(x)

	struct.extend([x for x in range(100, 110)])

	for x in struct:
		print(x)

