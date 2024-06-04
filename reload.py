#!/usr/bin/python
import some_text as st
print(st.text)

from importlib import reload
reload(st)
print(st.text)

from some_text import text
print(text)

exec(open('some_text.py').read())