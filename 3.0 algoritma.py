import os
import copy
import time

c = time.perf_counter()

path = "~/Desktop/Algoritma/questions.txt"
path1 = "~/Desktop/Algoritma/the_truman_show_script.txt"
question = open(os.path.expanduser(path), 'r')
script = open(os.path.expanduser(path1), 'r')
sorular = []
metin = []
stopwords = ["who", "is", "at", "of", "to", "the", "what", "does", "where", "how", "many", "time", "on", "as","a","his","her","an",
               "color"]


def match(word, arr):
    for i in range(len(arr)):
        if (arr[i][0:len(word)] == word):
            return i
    return -1


for line in script.read().split("."):
    metin.append(line.lower().split())
for line in question:
    line = line[0:len(line) - 2]
    sorular.append(line.lower().split())
question.close()
script.close()
del question, script, path1, path
text = metin
for sentence in sorular:
    print(' '.join(sentence))
    answer = copy.deepcopy(text)
    for words in sentence:
        if (words in stopwords):
            continue
        i = 0
        while i < len(answer):

            e = match(words, answer[i])
            if e != -1:
                answer[i].remove(answer[i][e])
                i = i + 1
            else:
                answer.remove(answer[i])
    if len(answer)!=1:
        answer.append("no answer")
    else:
        j= 0
        while j < len(answer[0]):

            if answer[0][j] in stopwords:
                answer[0].remove(answer[0][j])
            else:
                j = j + 1


    print(answer[0][0])
print(time.perf_counter() - c)