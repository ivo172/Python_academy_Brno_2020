words = 'A speech sound that is produced by comparatively open configuration of the vocal trajct.'
words = words.strip('.')
splited_wors = words.split()
print(splited_wors)

vowel_count = 0
cons_count = 0

for word in splited_wors:
    for char in word:
        if char == 'a':
            vowel_count = vowel_count + 1  
        if char == 'A':
            vowel_count = vowel_count + 1 
        if char == 'e':
            vowel_count = vowel_count + 1
        if char == 'i':
            vowel_count = vowel_count + 1
        if char == 'o':
            vowel_count = vowel_count + 1 
        if char == 'u':
            vowel_count = vowel_count + 1          
        else:
            cons_count = cons_count + 1
print(vowel_count, cons_count)    