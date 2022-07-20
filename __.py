#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv


# In[40]:


filename = 'C:\\Users\\GILBERT_SHYIRAMBERE\\Desktop\\Google\\weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)


# In[89]:


for index, column_header in enumerate(header_row):
    print(index, column_header)


# In[72]:


filename = 'C:\\Users\\GILBERT_SHYIRAMBERE\\Desktop\\Google\\weather.csv'

high_tmp = []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
        high = row[1]
        high_tmp.append(high)
    


# In[79]:


high_tmp = [float(i) for i in high_tmp]

print(high_tmp)


# In[80]:


import matplotlib.pyplot as plt


# In[82]:


# Plot the high temperatures.

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(high_tmp, c='red')

# Format plot.

plt.title("Daily high temperatures in x year", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


# In[94]:


filename = 'C:\\Users\\GILBERT_SHYIRAMBERE\\Desktop\\Google\\weather.csv'

rains = []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
        rain = row[2]
        rains.append(rain)


# In[95]:


rains = [float(i) for i in rains]

print(rains)


# In[97]:


# Plot the high temperatures.

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(rains, c='red')

# Format plot.

plt.title("Daily rain in x year", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


# In[ ]:




