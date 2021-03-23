#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# In[9]:


# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = '-RP2Ro876kKDy1by-5qK'


# Qaundl has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, we would prefer that you use the *requests* package, which can be easily downloaded using *pip* or *conda*. You can find the documentation for the package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any third party Python packages, such as *pandas*, and instead focus on what's available in the Python Standard Library (the *collections* module might come in handy: https://pymotw.com/3/collections/).
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, though some questions can also be answered using lists.
# You can read more on these data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# In[15]:


# First, import the relevant modules
# ran pip install quandl in the terminal here on paperspace
# requests was already installed
import quandl
import collections
import requests


# In[32]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned

#setting the api key
quandl.ApiConfig.api_key = API_KEY

# Frankfurt Stock Exchange has DATABASE_CODE = FSE
data = quandl.get("FSE/AFX_X", start_date="2017-12-29", end_date="2017-12-30") 
data.keys()


# In[41]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
print(data['Open'])
print(data['High'])
print(data['Low'])
print(data['Close'])
print(data['Change'])


# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[43]:


# 1)
data = quandl.get("FSE/AFX_X", start_date="2017-01-01", end_date="2017-12-31") 
data.keys()


# In[50]:


# 2)
#data['Open'] # we have 255 entries here. Float64 type 
#data['Open'][0] #returns the actual value here
#print(data['Daily Traded Units'][0])

# Create our own dictionary. Actually not too sure why this is necessary, maybe I am not understanding correctly what to do here.
equities = {
    'Open': data['Open'],
    'High': data['High'],
    'Low': data['Low'],
    'Close': data['Close'],
    'Change': data['Change'],
    'Close': data['Close'],
    'Change': data['Change'],
    'Traded Volume': data['Traded Volume'], 
    'Turnover': data['Turnover'],
    'Last Price of the Day': data['Last Price of the Day'],
    'Daily Traded Units': data['Daily Traded Units'], 
    'Daily Turnover': data['Daily Turnover'],
}


# In[59]:


# 3)
# Highest price
high = max(equities['High'])
print('Highest price: ' + str(high))

# Lowest price 
low = min(equities['Low'])
print('Lowest price: ' + str(low))


# In[70]:


# 4)
# Largest change in any one day (based on High and Low price)
max_change = max(equities['High'] - equities['Low'])
print('Max change in one day: ' + str(round(max_change, 3)))


# In[78]:


# 5)
# Largest change between any two days (based on Closing Price)
n = len(equities['Close'])
change2 = []
for c in range(0, n-1):
    change2.append(equities['Close'][c+1] - equities['Close'][c])

max_change2 = max(change2)
print("max change in two days: " + str(round(max_change2, 5)))


# In[82]:


# 6)
# Average daily trading volume during this year
avg_tv = sum(equities['Traded Volume']) / len(equities['Traded Volume'])
print("Average daily traded volume: " + str(round(avg_tv, 3)))


# In[95]:


# 7)
# Median trading volume during this year
tv_list = []
for elem in equities['Traded Volume']:
    tv_list.append(elem)

tv_list.sort()
median = tv_list[127]
print("Median traded volume: " + str(median))


# In[ ]:




