words = 'A speech sound that is produced by comparatively open configuration of the vocal trajct.'

count_vowels = 0
count_cons = 0
char = []
vowels = ('aeiouy')

print(words)

for char in words:
    if not char.isalpha():
        continue
    char = char.lower()
    if char in vowels:
        count_vowels = count_vowels + 1
    else: 
        count_cons = count_cons + 1
        
print(f'No. vowels: {count_vowels} No. consonants: {count_cons}')
