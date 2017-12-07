def halfway_captcha(string):

    s = 0

    for idx in xrange(1, len(string)):
        next_halfway = (idx + len(string) / 2) % len(string)

        if string[idx] == string[next_halfway]:
            s += int(string[idx])

    if string[0] == string[len(string) / 2]:
        s += int(string[0])

    return s


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f:
            print(halfway_captcha(line))
