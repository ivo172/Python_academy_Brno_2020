# Game Tic Tac Toe

print("Welcome to Tic Tac Toe\nGAME RULES:\nEach player can place one mark (or stone) per turn on the 3x3 grid\nThe "
      "WINNER is who succeeds in placing three of their marks in a\n* horizontal,\n* vertical or\n* diagonal row\nLet"
      "'s start the game")


def win(a, b, c):  # The function verifies that the assembly is victorious (3x the same stone)
    if a == b == c:
        return True


def horizont(str_line):
    a = str_line[0]
    b = str_line[1]
    c = str_line[2]
    win_h1 = win(a, b, c)
    a = str_line[3]
    b = str_line[4]
    c = str_line[5]
    win_h2 = win(a, b, c)
    a = str_line[6]
    b = str_line[7]
    c = str_line[8]
    win_h3 = win(a, b, c)
    if win_h1 or win_h2 or win_h3:
        return True


def vertical(str_line):
    a = str_line[0]
    b = str_line[3]
    c = str_line[6]
    win_v1 = win(a, b, c)
    a = str_line[1]
    b = str_line[4]
    c = str_line[7]
    win_v2 = win(a, b, c)
    a = str_line[2]
    b = str_line[5]
    c = str_line[8]
    win_v3 = win(a, b, c)
    if win_v1 or win_v2 or win_v3:
        return True


def diagonal(str_line):
    a = str_line[0]
    b = str_line[4]
    c = str_line[8]
    win_d1 = win(a, b, c)
    a = str_line[2]
    b = str_line[4]
    c = str_line[6]
    win_d2 = win(a, b, c)
    if win_d1 or win_d2:
        return True


str_ = '1', '2', '3', '4', '5', '6', '7', '8', '9'

a = str_[0]
b = str_[1]
c = str_[2]
d = str_[3]
e = str_[4]
f = str_[5]
g = str_[6]
h = str_[7]
i = str_[8]

print('----------------------')
print(f'|{a:^6}|{b:^6}|{c:^6}|')
print(f'|{d:^6}|{e:^6}|{f:^6}|')
print(f'|{g:^6}|{h:^6}|{i:^6}|')
print('----------------------')

while True:
    input_o = int(input('Player o | Please enter your move number:'))
    if input_o == 1:
          a = 'o'
    if input_o == 2:
          b = 'o'
    if input_o == 3:
          c = 'o'
    if input_o == 4:
          d = 'o'
    if input_o == 5:
          e = 'o'
    if input_o == 6:
          f = 'o'
    if input_o == 7:
          g = 'o'
    if input_o == 8:
          h = 'o'
    if input_o == 9:
          i = 'o'

    str_ = a + b + c + d + e + f + g + h + i
    print('----------------------')
    print(f'|{a:^6}|{b:^6}|{c:^6}|')
    print(f'|{d:^6}|{e:^6}|{f:^6}|')
    print(f'|{g:^6}|{h:^6}|{i:^6}|')
    print('----------------------')

    if diagonal(str_):
        print('Win o')
        exit()
    if horizont(str_):
        print('Win o')
        exit()
    if vertical(str_):
        print('Win o')
        exit()
    input_x = int(input('Player x | Please enter your move number:'))
    if input_x == 1:
          a = 'x'
    if input_x == 2:
          b = 'x'
    if input_x == 3:
          c = 'x'
    if input_x == 4:
          d = 'x'
    if input_x == 5:
          e = 'x'
    if input_x == 6:
          f = 'x'
    if input_x == 7:
          g = 'x'
    if input_x == 8:
          h = 'x'
    if input_x == 9:
          i = 'x'

    str_ = a + b + c + d + e + f + g + h + i

    print('----------------------')
    print(f'|{a:^6}|{b:^6}|{c:^6}|')
    print(f'|{d:^6}|{e:^6}|{f:^6}|')
    print(f'|{g:^6}|{h:^6}|{i:^6}|')
    print('----------------------')

    if diagonal(str_):
        print('Win x')
        exit()
    if horizont(str_):
        print('Win x')
        exit()
    if vertical(str_):
        print('Win x')
        exit()




