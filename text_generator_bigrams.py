from nltk.tokenize import regexp_tokenize, WhitespaceTokenizer
from nltk.probability import FreqDist
from nltk import bigrams
from collections import Counter
import random
import re
import numpy as np

t = WhitespaceTokenizer()
file_name = input()

with open(f"{file_name}", 'r', encoding="utf-8") as f, open("test.txt", 'w', encoding="utf-8") as output:
    text = f.read()
    # print(text)
    tokens = t.tokenize(text)
    # print(tokens[:100])
    bigrms = tuple(bigrams(tokens))
    bigrms_dict = Counter(bigrms)
    head_tails_dict = {}
    for item in bigrms_dict:
        head_tails_dict.setdefault(item[0], []).append((item[1], bigrms_dict[item]))
    # for item in head_tails_dict:
    #     if head_tails_dict[item] is []:
    #         print(item)
    # print(bigrms_dict, file=output)
    # print(bigrms, file=output)
    # print(len(head_tails_dict), file=output)
    # print(head_tails_dict, file=output)
    capital_tokens = [i for i in tokens[:-1] if re.match(r'^[A-Z].*[^.?!]$', i)]

    for i in range(10):
        head = random.choice(capital_tokens)
        sentence = [head]
        while len(sentence) < 5 or not re.match(r'.+[.?!]$', sentence[-1]):
            tails_list = [i[0] for i in head_tails_dict[head]]
            weights_list = [i[1] for i in head_tails_dict[head]]
            next_word = ''.join(random.choices(tails_list, weights_list))
            sentence += [next_word]
            head = next_word

        print(' '.join(sentence))
        print(' '.join(sentence), file=output)





# print(f"Number of bigrams: {len(bigrms)}")
# print(bigrms[:100])
# print("Corpus statistics")
# print(f"All tokens: {FreqDist(tokens).N()}")
# print(f"Unique tokens: {FreqDist(tokens).B()}")



# while True:
#     s = input()
#     if s == 'exit':
#         break
#     print(f"Head: {s}")
#     try:
#         for item in head_tails_dict[s]:
#             print(f"Tail: {item[0]} Count: {item[1]}")
#     except KeyError:
#         print("Key Error. The requested word is not in the model. Please input another word.")



# while True:
#     try:
#         n = input()
#         if n == "exit":
#             break
#         print(tokens[int(n)])
#     except IndexError:
#         print("Index Error. Please input an integer that is in the range of the corpus.")
#         continue
#     except TypeError:
#         print("Type Error. Please input an integer.")
#         continue
#     except ValueError:
#         print("Value Error. Please make it work! (:")
#         continue
#     except Exception:
#         print("Error. Think about it!")
#         continue
# while True:
#     try:
    #     n = input()
    #     if n == "exit":
    #         break
    #     n = int(n)
    #     print(f"Head: {bigrms[n][0]}     Tail: {bigrms[n][1]}")
    #     # print(tokens[int(n)])
    # except IndexError:
    #     print("Index Error. Please input an integer that is in the range of the corpus.")
    #     continue
    # except TypeError:
    #     print("Type Error. Please input an integer.")
    #     continue
    # except ValueError:
    #     print("Value Error. Please make it work! (:")
    #     continue
    # except Exception:
    #     print("Error. Think about it!")
    #     continue
