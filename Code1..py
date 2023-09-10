#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# prevalence 
population = int(input("Population:"))
exsistingcases = int(input("Exsisting cases:"))
prevelance = exsistingcases / population
print(prevelance)
print(prevelance * 100000)


# In[ ]:


# incidence 
newcases = int(input("New cases: "))
incidence = newcases / population
print(incidence)
print(incidence * 100000)


# In[ ]:


# mortality rate 
dead = int(input("Number of those who died: "))
segment = int(input("Number of those who had the disease: "))
mortalityrate = dead / segment 
print(mortalityrate)
print(mortalityrate * 100000)


# In[26]:


# years of potential life lost 
lifeexpectancy = 77
ages = [32,45,28,37,52]
print(lifeexpectancy - ages[0])
print(lifeexpectancy - ages[1])
print(lifeexpectancy - ages[2])
print(lifeexpectancy - ages[3])
print(lifeexpectancy - ages[4])


# In[27]:


#yppl 
lifelost = [45,32,49,40,25]
yppl= sum(lifelost) / len(lifelost)
print(yppl)


# In[ ]:





# In[ ]:




