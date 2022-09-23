from corpus_loader import word_list, name_list

sentences = [
    'A dark and stormy night',
    'jdh jduwu iu jhdf jhsd jokf jgij sdfls dff',
    'It was the best of times'
]

# max (3) -> pda
# max (5) -> rfc
# max (7) -> the

for sentence in sentences:
    print(sentence)
    for word in sentence.split():
        print(word)
        if word in word_list:
            print(f'Yep,{word} is there!')
        else:
            print(f'Nope, {word} not there')
