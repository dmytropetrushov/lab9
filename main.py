import nltk
import math
from nltk.corpus import brown
from nltk.corpus import wordnet

print('#2')
host_synset = wordnet.synset('host.n.01')
sobersides_synset = wordnet.synset('sobersides.n.01')

lowest_common_hypernyms = host_synset.lowest_common_hypernyms(sobersides_synset)
print("Наименьший общий гипероним:", lowest_common_hypernyms)
hyponyms = lowest_common_hypernyms[0].hyponyms()
print("Список всех понятий, являющихся дочерними узлами найденного наименьшего общего гиперонима:", hyponyms)

wordbr = 0
sum_words = len(brown.words(brown.fileids()))
for synset1 in hyponyms:
    for word in brown.words(brown.fileids()):
        for lemma_name in synset1.lemma_names():
            if word == lemma_name:
                wordbr += 1

information_content = wordbr / sum_words
print("Информационное содержание найденного наименьшего общего гиперонима:", information_content)
reznik_similarity = -1 * math.log(information_content)
print("Семантическая близость двух понятий согласно методу Резника:", reznik_similarity)

print('\n#1')
max_similarity = 0
for i in wordnet.synsets('hostess'):
    for j in wordnet.synsets('liberal'):
        similarity = i.path_similarity(j)
        print(similarity)
        if similarity is not None and similarity > max_similarity:
            max_similarity = similarity

print('------------------')

max1_similarity = 0
for i in wordnet.synsets('host'):
    for j in wordnet.synsets('hostess'):
        similarity = i.path_similarity(j)
        print(similarity)
        if similarity is not None and similarity > max1_similarity:
            max1_similarity = similarity

print('------------------')

print('hostess | liberal')
print(max_similarity)
print('host | hostess')
print(max1_similarity)

print('\n#3')
print("Введите два синсета корпуса Brown (через enter):")
synset_a = input()
synset_b = input()

t = wordnet.synset(synset_a).lowest_common_hypernyms(wordnet.synset(synset_b))
print("Наименьший общий гипероним:", t)
hyponyms = t[0].hyponyms()
print("Список всех понятий, являющихся дочерними узлами найденного наименьшего общего гиперонима:", hyponyms)

wordbr = 0
sum_words = len(brown.words(brown.fileids()))
for synset1 in hyponyms:
    for word in brown.words(brown.fileids()):
        for lemma_name in synset1.lemma_names():
            if word == lemma_name:
                wordbr += 1

information_content = wordbr / sum_words
print("Информационное содержание найденного наименьшего общего гиперонима:", information_content)
reznik_similarity = -1 * math.log(information_content)
print("Семантическая близость двух понятий согласно методу Резника:", reznik_similarity)
