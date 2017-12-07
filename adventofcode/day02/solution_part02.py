def evenly_divisible(array):
    sorted_array = list(reversed(sorted(array)))

    for idx1 in xrange(len(sorted_array) - 1):
        for idx2 in xrange(1, len(sorted_array)):
            a = float(sorted_array[idx1])
            b = float(sorted_array[idx2])
            result = divmod(a, b)
            if (result[0] != 1.0) and (result[1] == 0.0):
                # print(a, b, result)
                return result[0]
            # if result[1] == 0.0:
                # return result[0]

    return None


def sum_evenly_divided(spreadsheet):
    return sum(evenly_divisible(sline) for sline in spreadsheet)


if __name__ == '__main__':
    spreadsheet = []
    with open('input.txt', 'r') as f:
        for line in f:
            array = [int(element) for element in line.split('\t')]
            spreadsheet.append(array)

    print(sum_evenly_divided(spreadsheet))
