import random

words = {'articles' : ('the', 'a', 'an'), 'determiners' : ('another', 'this', 'every', 'many'), 
        'subjects' : ('cat', 'dog', 'man', 'woman'), 'verbs' : ('sang', 'ran', 'jumped'), 
        'adverbs' : ('loudly', 'quietly', 'well', 'badly')}

combine = [['article', 'subject', 'verb', 'adverb'], ['determiner', 'subject', 'verb'], ['determiner', 'subject', 'verb', 'adverb']]

def lore_poetry(num_row):
    i = []
    rows = []
    if i in range(num_row):
        row = []
        combine = random.choice(combine)
        for comb in combine:
            row.append(random.choice(words[comb]))
        rows.append(''.join(row))
    result = '\n'.join(rows)
    return result

poetry = lore_poetry(8)
