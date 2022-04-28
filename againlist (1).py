#!/usr/bin/env python
# coding: utf-8

# In[26]:


from collections import Counter
def anagran(first , secend):
    return Counter(first) == Counter(secend)

anagran("abcd3","3acdb") #True

