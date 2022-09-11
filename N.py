import re
import random

word1n = {}
word2n = {}

class Model:
    def __init__(self, text):
        self.text = text
        self.word1n = {}
        self.word2n = {}
        print('----------------------------------------')
        self.training_1n()
        self.training_2n()

    def training_1n(self):
        for sentence in self.text:
            objects = sentence.split()

            for pref in range(0, len(objects) - 2):
                if objects[pref] in self.word1n:
                    key = objects[pref]
                    meaning = self.word1n[key]

                    worl = True
                    for i in meaning:
                        if i[0] == objects[pref + 1]:
                            i[1] = i[1] + 1
                            worl = False
                    if worl:
                        meaning.append([objects[pref + 1], 1])
                else:
                    self.word1n[objects[pref]] = [[objects[pref + 1], 1]]

    def training_2n(self):
        for sentence in self.text:
            objects = sentence.split()

            for pref in range(1, len(objects) - 2):
                if ' '.join(objects[pref - 1:pref + 1]) in self.word2n:
                    key = ' '.join(objects[pref - 1:pref + 1])
                    meaning = self.word2n[key]

                    worl = True
                    for i in meaning:
                        if i[0] == objects[pref + 1]:
                            i[1] = i[1] + 1
                            worl = False
                    if worl:
                        meaning.append([objects[pref + 1], 1])
                else:
                    self.word2n[' '.join(objects[pref - 1:pref + 1])] = [[objects[pref + 1], 1]]

    def selection(self):
        while True:
            pref = input('Введите одно или два слова: ').lower()

            if pref == 'закрыть':
                break

            if len(pref.split()) == 2:
                if pref in self.word2n:
                    n = 0
                    st = ''
                    for i in self.word2n[pref]:
                        if i[1] > n:
                            n = i[1]
                            st = i[0]
                    print(pref + ' ' + st)
                else:
                    print(pref + ' ' + self.word2n[random.choice(list(self.word2n))][0][0])

            elif len(pref.split()) == 1:
                if pref in self.word1n:
                    n = 0
                    st = ''
                    for i in self.word1n[pref]:
                        if i[1] > n:
                            n = i[1]
                            st = i[0]
                    print(pref + ' ' + st)
                else:
                    print(pref + ' ' + self.word1n[random.choice(list(self.word1n))][0][0])

            else:
                print('Попробуйте ещё раз')






with open('тексты/1.txt', 'r', encoding="utf-8") as f:
    text1 = f.read().lower().replace('!', '.').replace('?', '.').replace('\n', '')
    text1 = text1.split('.')
    text = []
    for i in text1:
        i = re.sub('[^A-Za-zА-Яа-я]+', ' ', i)
        i = re.sub(' +', ' ', i)
        if i != '' and len(i) > 1:
            if i[1] == ' ':
                text.append(i[2:])
            elif i[0] == ' ':
                text.append(i[1:])
            else:
                text.append(i)

    f.close()

model = Model(text)
model.selection()
