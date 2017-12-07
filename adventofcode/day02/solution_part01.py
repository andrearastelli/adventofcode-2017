def checksum_line(array):
    return max(array) - min(array)


def checksum(spreadsheet):
    return sum(checksum_line(line) for line in spreadsheet)


if __name__ == '__main__':
    spreadsheet = []
    with open('input.txt', 'r') as f:
        for line in f:
            array = [int(element) for element in line.split('\t')]
            spreadsheet.append(array)

    print(checksum(spreadsheet))
