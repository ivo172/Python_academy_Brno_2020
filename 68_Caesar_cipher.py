def caesar(message, offset):
    message_ = list(message.lower())
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alpha = dict(enumerate(alphabet))
    result = ''
    for char in message:
        index = alphabet.index(char)
        result = result + alpha.get(index + offset)
    return result


print(caesar('kolo', 2))
