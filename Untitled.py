#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import Counter
def anagran(four , five ):
    import sys
    print(sys.getsizeof(four , five))#24
    return Counter(four) == Counter(five)
anagran("abcde","badec")


# In[4]:


import sys 


# In[ ]:




