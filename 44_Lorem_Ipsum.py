import random

words = {'article': ('the', 'a', 'an'), 'determiner': ('another', 'this', 'every', 'many'),
         'subject': ('cat', 'dog', 'man', 'woman'), 'verb': ('sang', 'ran', 'jumped'),
         'adverb': ('loudly', 'quietly', 'well', 'badly')}

combines = [['article', 'subject', 'verb', 'adverb'], ['determiner', 'subject', 'verb'],
           ['determiner', 'subject', 'verb', 'adverb']]


def lore_poetry(num_row):
    rows = []
    for _ in range(num_row):
        row = []
        combin = random.choice(combines)
        for comb in combin:
            row.append(random.choice(words[comb]))
        rows.append(' '.join(row))
    result = '\n'.join(rows)
    print(result)
    return result
