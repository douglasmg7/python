#!/usr/bin/env python

import nltk

text = nltk.Text(nltk.corpus.state_union.words())
#  text.concordance('america', lines=5)

concordance_list = text.concordance_list('america', lines=2)
for item in concordance_list:
    print(item.line)