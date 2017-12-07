
def inverse_captcha(string):

    s = 0

    for idx in range(1, len(string)):
        # print(string[idx], string[idx-1])

        if string[idx] == string[idx - 1]:
            s += int(string[idx])

    if string[-1] == string[0]:
        s += int(string[0])

    return s


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f:
            print(inverse_captcha(line))
