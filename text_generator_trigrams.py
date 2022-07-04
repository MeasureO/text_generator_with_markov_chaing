from nltk.tokenize import regexp_tokenize, WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk import bigrams
from nltk import trigrams
from nltk.util import ngrams
from collections import Counter
import random
import re
import numpy as np
N = 3

t = WhitespaceTokenizer()
file_name = input()

with open(f"{file_name}", 'r', encoding="utf-8") as f, open("test.txt", 'w', encoding="utf-8") as output:
    text = f.read()
    # print(text)
    tokens = t.tokenize(text)
    # print(tokens[:100])
    bigrms = tuple(bigrams(tokens))
    bigrms_dict = Counter(bigrms)
    ngrms = tuple(ngrams(tokens, N))
    # print(ngrms, file=output)
    ngrms_dict = Counter(ngrms)
    # print(ngrms_dict, file=output)
    head_tails_dict = {}
    for item in ngrms_dict:
        head_tails_dict.setdefault((item[0], item[1]), []).append((item[2], ngrms_dict[item]))
    # for item in head_tails_dict:
    #     if head_tails_dict[item] is []:
    #         print(item)
    # print(bigrms_dict, file=output)
    # print(bigrms, file=output)
    # print(len(head_tails_dict), file=output)
    print(head_tails_dict, file=output)
    capital_tokens = [i for i in bigrms if re.match(r'^[A-Z].*[^.?!]$', i[0])]
    print(capital_tokens, file=output)
    for i in range(10):
        head = random.choice(capital_tokens)
        sentence = [head[0], head[1]]
        while len(sentence) < 5 or not re.match(r'.+[.?!]$', sentence[-1]):
            tails_list = [i[0] for i in head_tails_dict[head]]
            weights_list = [i[1] for i in head_tails_dict[head]]
            next_word = ''.join(random.choices(tails_list, weights_list))
            sentence += [next_word]
            head = (head[1], next_word)

        print(' '.join(sentence))
        print(' '.join(sentence), file=output)



