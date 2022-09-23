def warmup1(num):
    for i in range(num):
        # handle 0
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def warmup2(num):
    print('\n'.join('* ' * i for i in range(num + 1)))


warmup1(10)
warmup2(5)
