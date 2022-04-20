data = ['london','Moscow','Amsterdam']
mabyRightWord = ''
rightWord = ''
rightWords = []
countWord_1 = 0
countWord_2 = 0
inputWord = 'oscow'
countRightLetters = 0

for i in range(len(data)):

    word_1 = data[i] #word_1 - слово с минимальным кол-во букв из двух слов,которые будут сравниваться
    word_2 = inputWord #word_2 - слово с максимальным кол-во букв среди двух слов, которые будут сравниваться

    for j in range(len(word_1)):
        for n in range(len(word_2)):
            let_1 = word_1[j]
            let_2 = word_2[n]
            if mabyRightWord != '':
                if mabyRightWord.count(word_2[n]) < word_1.count(word_2[n]) and word_1[j] == word_2[n]:
                    mabyRightWord += word_2[n]
            else:
                if word_1[j] == word_2[n]:
                    mabyRightWord += word_2[n]

    if len(mabyRightWord) > len(rightWord):
        rightWord = mabyRightWord
    mabyRightWord = ''



print(rightWords)
print(rightWord)
# print(type(len(inputWord)))


# for i in range(len(data)-1):
#     word_1 = data[i]
#     word_2 = data[i+1]
#     for i in range(len(word_1)):
#         if word_1[i] == inputWord[i]:
#             countWord_1 += 1
#     for i in range(len(word_2)):
#         if word_2[i] == inputWord[i]:
#             countWord_2 += 1
#
#     if countWord_1 > countWord_2 and countWord_1 > countRightLetters:
#         rightWord = word_1
#         countRightLetters = countWord_1
#
#     if countWord_2 > countWord_1 and countWord_1 > countRightLetters:
#         rightWord = word_2
#         countRightLetters = countWord_1
#
#     if countWord_2 == countWord_1 and countWord_1 > countRightLetters:
#         rightWords.append(word_1)
#         rightWords.append(word_2)
#         countRightLetters = countWord_1
#
#     countWord_1 = 0
#     countWord_2 = 0

