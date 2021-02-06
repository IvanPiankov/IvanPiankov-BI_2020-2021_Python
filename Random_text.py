import random


str_text = input()
text = str_text.split()
new_text = []
for i in text:
    if len(i) > 3:
        str_word = list(i)
        first_elem = str_word[0]
        last_elem = str_word[-1]
        str_word = str_word[1:-1]
        random.shuffle(str_word)
        str_word.append(last_elem)
        str_word.insert(0, first_elem)
        word = "".join(str_word)
        new_text.append(word)
    else:
        new_text.append(i)
print(" ".join(new_text))



