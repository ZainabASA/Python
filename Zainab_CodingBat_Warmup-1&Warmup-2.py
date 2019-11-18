#!/usr/bin/env python
# coding: utf-8

# # Warmup-1

# ### sleep_in

# In[5]:


def sleep_in(w, v):
    if w==False and v== False:
        return True
    elif w==False or v== True:
        return True
    else:
        return False


# In[6]:


sleep_in(False, False)


# In[7]:


sleep_in(True, False)


# In[8]:


sleep_in(False, True)


# ### diff21 

# In[9]:


def diff21(n):
    if n>=21:
        return abs(n-21) *2
    else:
        return abs(n-21) 


# In[11]:


diff21(19)


# In[12]:


diff21(21)


# ### parrot_trouble

# In[2]:


def parrot_trouble(talking, hour):
    if(talking==1 and (hour>7 or hour<20)):
        return True
    else:
        return False


# In[4]:


parrot_trouble(True,6)


# ### makes10

# In[ ]:


def makes10(a, b):
    if(a ==10 or b ==10 or (a+b)==10):
        return True
    else:
        return False


# In[19]:


makes10(9,11)


# ### near_hundred

# In[24]:


def near_hundred(n):
    if (n-100) <10 or (n-200) <10:
        return True
    else:
        return False
    


# In[25]:


near_hundred(110)


# In[26]:


near_hundred(220)


# ### pos_neg

# In[15]:



def pos_neg(a, b, negative):
    if (a<0 and  b<0) and negative==True:
        return True
    else:
        return False
    


# In[ ]:





# In[18]:


pos_neg(1, -1, False) 


# ### sum_double

# In[5]:


def sum_double(a, b):
    if(a==b):
        return (a+b)*2
    else:
        return (a+b)


# ### front3 

# In[21]:


def front3(strr):
    res=" "
    if len(strr)<=3:
        for i in range(3):
            res=res+strr
        print (res)
    else:
        st=" "
        list(strr)
        for i in range(3):
            r=strr[0:3]
            st=st+r
        print (st)


# In[ ]:





# In[22]:


front3('Java')


# ### monkey_trouble

# In[27]:


def monkey_trouble(a_smile, b_smile):
    if (a_smile==1 and a_smile==1) or (a_smile==0 and a_smile==0):
        return True
    else:
        return False


# In[28]:


monkey_trouble(True, True)


# ### front_back

# In[29]:


def front_back(strr):
    newstr=" "
    f=strr[0]
    l=strr[-1]
    return strr[-1]+strr[1:-1]+strr[0]
    


# In[31]:


front_back('code')


# In[32]:


front_back('Zainab')


# ### missing_char

# In[72]:


def missing_char(strr, n):
    #newstrr=list(strr)
    print(strr)
    print (strr[n])
    return strr.replace(strr[n], "")


# In[73]:


missing_char('Zainab',2)


# # Warmup-2

# ### string_times
# 

# In[76]:


def string_times(strr, n):
    for i in range(0,n):
        print (strr)


# In[77]:


def string_times(strr, n):
    return strr*n


# In[78]:


string_times('za',2)


# ### front_times

# In[2]:


def front_times(strr, n):
    res=" "
    if len(strr)<=3:
        for i in range(1,n+1):
            res=res+strr
        print (res)
    else:
        st=" "
        list(strr)
        for i in range(0,n):
            r=strr[0:3]
            st=st+r
        print (st)
        


# In[5]:


front_times('zaa',2)


# In[4]:


front_times('fffza',5)


# ### array123 

# In[94]:


def array123(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
        


# In[96]:


arr=[1, 1, 2, 3, 1]
array123(arr)


# ### array_count9

# In[101]:


def array_count9(nums):
    ct=0
    for i in range(0,len(nums)):
        if nums[i]==9:
            ct=ct+1
    return ct


# In[102]:


array_count9([1, 9, 9, 3, 9])


# ### string_bits

# In[ ]:



def string_bits(str):
    return str[0:len(str):2]


# In[120]:


string_bits('Zainab')


# In[ ]:




