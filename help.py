def generate_checkerboard(x, y):
    result = [] #result is a list of lists

    for j in range(0, y):
        temp = []
        for i in range(0, x):
            temp.append((i + j) % 2)
        result.append(temp)

    return result