sentence = 'The exercise was done correctly'
print(len(sentence))
print(sentence.lower())
letters = 'aeiou'
count = 0
for i in sentence:
    if i in letters:
        count += 1
print(count)
sentence = sentence.replace('ugly', 'beauty')
print(sentence)
if (sentence.startswith('The')):
    print('Предложение начинается на "The" ')
else:
    print('Не начинается на "The"')
if (sentence.endswith("end")):
    print('Кончается на "end" ')
else:
    print('Но не заканчивается на "end"')