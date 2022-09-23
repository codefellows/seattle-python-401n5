# file = open('assets/spam.txt')
# print(file)

# contents = file.read()
# print(contents)
# for char in contents:
#     print(char)

# print('Is the file close?', file.closed)
# file.close()
# print('Is the file close?', file.closed)

# with open('assets/spam.txt') as file:
#     print(file.read())

# print('Is the file close?', file.closed)

# print(help(file))

# print(dir(file))

with open('assets/brain.jpg', 'rb') as f:
    contents = f.read()
    # print(contents)

with open('assets/brain_copy.jpg', 'wb') as f2:
    f2.write(contents)

# with open('assets/brain_copy.jpg', 'rb') as f3:
#     content2 = f3.read()
#     print(content2)
