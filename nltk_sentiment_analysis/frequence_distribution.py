#!/usr/bin/env python

import nltk
from pprint import pprint

#  nltk.download([
    #  'shakespeare',
    #  'names',
    #  'stopwords',
    #  'state_union',
    #  'twitter_samples',
    #  'movie_reviews',
    #  'averaged_perceptron_tagger',
    #  'vader_lexicon',
    #  'punkt',
    #  ])

# not working
#  w = nltk.corpus.shakespeare.words()

#  words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
#  stopwords = nltk.corpus.stopwords.words('english')

#  words = [w for w in words if w.lower() not in stopwords]
#  for i in range(100):
    #  print(words[i])

text = """
For some quick analysis, creating a corpus could be overkill.
If all you need is a word list,
there are simpler ways to achieve that goal.
some some some some"""
#  pprint(nltk.word_tokenize(text), width=79, compact=True)

#  words = nltk.word_tokenize(text)
words: list[str] = nltk.word_tokenize(text)
fd = nltk.FreqDist(words)

print(fd.most_common(3))
print(fd.tabulate(3))
print(fd['some'])

lower_fd = nltk.FreqDist([w.lower() for w in fd])
for w in lower_fd:
    print(w)

#  words: list[str] = nltk.word_tokenize(text)
#  fd = nltk.FreqDist(words)