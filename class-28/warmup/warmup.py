POINTS = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
    'z': 10
}


def score(word):
    score_total = 0
    if not word:
        return score_total
    for letter in word.lower():
        if letter.isalpha():
            score_total += POINTS[letter]
    return score_total

# w = 4 o = 1 r = 1 = 2: Total: 8


print(score('word'))  # 8
print(score('w0rd'))  # 7
print(score('a word'))  # 9
print(score('k h klas nsd s kljhh lihsdf '))


    # non letter


    # Testing
    # happy path just letters
    # something with a non alpha char in it.
    # and empty string
    # space? a farm
