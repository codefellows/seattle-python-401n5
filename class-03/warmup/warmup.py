# Given a string, write a function that returns a new string but only has one of each character
# Example: 'commissioner'
# Return: 'comisner'

def remove_duplicates1(my_str):
    new_string = ''
    tmp_list = []
    for char in my_str:
        if char not in tmp_list:
            tmp_list.append(char)
            new_string += char
    return new_string


def remove_duplicates2(my_str):
    new_string = set(my_str)
    return "".join(new_string)


if __name__ == '__main__':
    my_string = 'cOmmissionerOo'
    print(remove_duplicates2(my_string))

    # print(set(my_string))

name = ['Roger', 'Jae', 'Tony', 'Roger']
print(set(name))
