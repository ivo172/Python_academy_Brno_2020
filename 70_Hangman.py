# The goal of this exercise is to implement the hangman game. The game is
# played by 2 players, in this case by the computer and the human. The
# computer selects a secret word and the human tries to guess it by
# suggesting letters or numbers, within a certain number of guesses.
# The word to guess is represented by a row of dashes, representing each
# letter of the word.
# Each time the human player suggests a letter that is not present in the
# guessed word, the counter of incorrect guesses is increased by one.
# Computer wins and the game ends if the number of incorrect guesses reaches
# specified amount. The human wins if the whole word is guessed before
# reaching the limit of incorrect guesses.
# You shall decide what the limit of incorrect guesses should be.


def main_game(word):
    guesses_available = len(word) * 2
    print('I am thinking of a word. What word is it?')
    ground_line = (len(word) * "_")  # Create line ___ how length is word
    print(ground_line)
    while guesses_available > 0:
        print(f"({guesses_available} guesses available)")
        guesses_available = guesses_available - 1
        inp_char = input('Guess a letter: ')
        index = 0
        if inp_char in word:
            count_char = word.count(inp_char)
            while index < len(word):
                index = word.find(inp_char, index)
                if index == -1:
                    break
                ground_line = ground_line[:index] + inp_char + ground_line[
                                                           index + 1:]
                index += 1
            print(f'Yes, there is {count_char} letter "{inp_char}".')
            print(ground_line)
            over = ground_line.find('_')
            if over == -1:
                print('Victory !!!')
                exit()
        else:
            print(f'No, the letter "{inp_char}" is not in my word')
            print(ground_line)
    print('Game over')


main_game('Full')
