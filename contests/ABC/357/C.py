def create_carpet(level):
    if level == 0:
        return ["#"]
    smaller_carpet = create_carpet(level - 1)
    size = len(smaller_carpet)

    new_size = size * 3
    new_carpet = [["." for _ in range(new_size)] for _ in range(new_size)]

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for x in range(size):
                for y in range(size):
                    new_carpet[i * size + x][j * size + y] = smaller_carpet[x][y]

    return ["".join(row) for row in new_carpet]

N = int(input())

carpet = create_carpet(N)

for row in carpet:
    print(row)