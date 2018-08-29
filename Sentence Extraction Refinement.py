
# coding: utf-8

# In[64]:


import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict


# In[65]:


url = "http://www.elevate-hr.com/about-us/"


# In[66]:


# perform GET request to target url
r = requests.get(url)
s = BeautifulSoup(r.text, "lxml")


# In[108]:


# s.getText(separator=u' ');

# # get contents in <body> tag
# bod = s.find('body')


# In[69]:


# substitute extra whitespace with single newline
bod_sub = re.sub(r'(\t|\n|\s)*\n(\t|\n|\s)*', '\n\n',s.getText(separator=u' '))
# strip trailing whitespace
bod_sub = bod_sub.strip()


# In[70]:


bod_sub;


# In[89]:


# replace newlines
# bod_stripped = bod_sub.replace('(.|!|?)\n', '. ')
bod_stripped = bod_sub.replace('.\n', '. ')
bod_stripped = bod_stripped.replace('!\n', '. ')
bod_stripped = bod_stripped.replace('Inc.', 'Incorporated')
bod_stripped = bod_stripped.replace('?\n', '. ')


# In[99]:


bod_stripped


# In[100]:


# takes care of sentences that dont' end with periods- extra newline blocks were
# replaced by a single newline in line 15
bod_s = re.sub(r'(([a-z])|([A-Z]))+\n(([a-z])|([A-Z]))+', ' ',bod_stripped)
stripped_newlines = bod_s.replace('\n\n', '. ')
stripped_newlines = bod_s.replace('\n', ' ')


# In[101]:


stripped_newlines


# In[102]:


# strip any remaining trailing whitespace (probably unnecessary)
stripped_newlines = stripped_newlines.strip()


# In[103]:


stripped_newlines;


# In[104]:


# split by sentences and add back period at the end of each sentence
stripped = stripped_newlines.split('.')
stripped = [(strip + '.') for strip in stripped]


# In[105]:


stripped;


# In[106]:


cleaned = []
for strip in stripped:
    separated = strip.split(' ')
    if "function" not in strip and len(separated) > 3:
        if "{" not in strip:
            if "$(" not in strip:
                if ");" not in strip:
                    if "href" not in strip:
                        cleaned.append(strip.strip())

# text, arr = get_sentences("https://asana.com/company")
# print(text)


# In[107]:


cleaned

