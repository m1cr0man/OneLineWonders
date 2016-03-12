print("".join([(__import__("sys").argv[1][i:i + 2])[::-1] for i in range(0, len(__import__("sys").argv[1]),2)]))
