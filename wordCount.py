word_dict = {}

sentence = input("Text: ")
sentence = sentence.split()

for word in sentence:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
for word, count in sorted(word_dict.items()):
    print("{} : {}".format(word, count))