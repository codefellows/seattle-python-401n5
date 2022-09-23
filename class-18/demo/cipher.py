# create a function that will take a string, encrypt
# it by xx amount

# create a function that takes a string and a shift number
# Shift the string by the shift number
# return the shifted number

def encrypt(string_number, key):
    # 1234, 3 - > 4567
    # split the string
    # whole numbers from 0-9
    # iterate
    # do? shift
    shifted_value = ''
    for num in string_number:
        temp_val = int(num) + key
        print(temp_val)
        #1234
        # while temp_val > 9:
        #     temp_val -= 10
        # shifted_value += str(temp_val)
        shifted_value += str(temp_val % 10)
    return shifted_value


def decrypt(encoded_msg, key):
    return encrypt(encoded_msg, -key)


if __name__ == '__main__':
    # test1 = encrypt("1234", 3)
    # print(test1)
    # test2 = encrypt('789', 3)
    # print(test2)
    # test3 = encrypt('123', 7236)
    # print(test3)
    # test4 = decrypt('4567', 3)
    # print(test4)
    test5 = decrypt('1234', 3)
    print(test5)
