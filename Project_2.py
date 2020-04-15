# Game Tic Tac Toe

print('Welcome to Tic Tac Toe\nGAME RULES:\nEach player can place one mark (or stone) per turn on the 3x3 grid\nThe '
      'WINNER is who succeeds in placing three of their marks in a\n* horizontal,\n* vertical or\n* diagonal row\nLet'
      '\'s start the game')


def win(a, b, c):       # The function verifies that the assembly is victorious (3x the same stone)
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


str_ = '1','2','3','4','5','6','7','8','9'

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

win_horizontal = horizont(str_)
win_vertical = vertical(str_)
win_diagonal = diagonal(str_)

if win_horizontal or win_vertical or win_diagonal:
      print('WINNER')
