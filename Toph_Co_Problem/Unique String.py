a_string = input()
lowercase = a_string.lower()
vowel_counts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
counts = vowel_counts.values()
total_vowels = sum(counts)
if total_vowels >2:
    print('YES')
else:
    print('NO')
    