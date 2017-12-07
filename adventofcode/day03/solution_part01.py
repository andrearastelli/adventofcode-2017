"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  24  25
"""

import math
import pprint


def build_spiral(last_number):
    square_side = int(math.sqrt(last_number))
    pprint.pprint(square_side)

    if (square_side % 2) == 0:
        square_side += 1

    matrix = [[0 for i in range(square_side)] for i in range(square_side)]
    pprint.pprint(matrix)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    counter = 0

    spiral = 0
    x = square_side // 2
    y = square_side // 2 - 1
    pprint.pprint((x, y))

    for i in range(square_side):
        for j in range(square_side):
            spiral = i % 4
            x += dx[spiral]
            y += dy[spiral]
            pprint.pprint(((i, j), (x, y)))
            counter += 1
            try:
                matrix[x][y] = counter
            except:
                pass

    pprint.pprint(matrix)


def manhattan_steps(destination):
    matrix = build_spiral(destination)
    return 0


if __name__ == '__main__':
    print build_spiral(10)
    # print(manhattan_steps(288678))
