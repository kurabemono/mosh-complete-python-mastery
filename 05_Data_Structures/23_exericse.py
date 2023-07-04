sentence = "This is a common interview question"

letters = dict()

for letter in sentence:
    ch = letter.lower()
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

print(sorted([*letters.items()], key=lambda item: item[1], reverse=True)[0])
