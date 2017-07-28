
# coding: utf-8

# # Assignment 2 - Pandas Introduction
# All questions are weighted the same in this assignment.
# ## Part 1
# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry on [All Time Olympic Games Medals](https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table), and does some basic data cleaning. 
# 
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals, total # number of games, total # of medals. Use this dataset to answer the questions below.

# In[1]:

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df


# ### Question 0 (Example)
# 
# What is the first country in df?
# 
# *This function should return a Series.*

# In[2]:

# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 


# ### Question 1
# Which country has won the most gold medals in summer games?
# 
# *This function should return a single string value.*

# In[3]:

def answer_one():
    # Since the index is name of countries
    country = df['Gold'].idxmax()
    return country

answer_one()


# ### Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# 
# *This function should return a single string value.*

# In[4]:

def answer_two():
    max_diff = 0
    for ct, row in df.iterrows():
        diff = abs(row['Gold'] - row['Gold.1'])
        if diff > max_diff:
            max_diff = diff
            max_diff_country = ct
    return max_diff_country

answer_two()


# ### Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? 
# 
# $$\frac{Summer~Gold - Winter~Gold}{Total~Gold}$$
# 
# Only include countries that have won at least 1 gold in both summer and winter.
# 
# *This function should return a single string value.*

# In[5]:

def answer_three():
    has_gold_df = df[df['Gold.1'] > 0][df['Gold'] > 0]
    max_diff_ratio = 0 
    for ct, row in has_gold_df.iterrows():
        diff_ratio = abs((row['Gold'] - row['Gold.1']) / row['Gold.2'])
        if diff_ratio > max_diff_ratio:
            max_diff_ratio = diff_ratio
            max_diff_country = ct
    return max_diff_country

answer_three()


# ### Question 4
# Write a function to update the dataframe to include a new column called "Points" which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze mdeals for 1 point. The function should return only the column (a Series object) which you created.
# 
# *This function should return a Series named `Points` of length 146*

# In[6]:

def answer_four():
    points_list = []
    for ct, row in df.iterrows():
        points_list.append(row['Gold.2'] * 3 + row['Silver.2'] * 2 + row['Bronze.2'] * 1)
    Points = pd.Series(points_list, index=df.index)
    df['Points'] = Points.values
    return Points


# ## Part 2
# For the next set of questions, we will be using census data from the [United States Census Bureau](http://www.census.gov/popest/data/counties/totals/2015/CO-EST2015-alldata.html). Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. [See this document](http://www.census.gov/popest/data/counties/totals/2015/files/CO-EST2015-alldata.pdf) for a description of the variable names.
# 
# The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.
# 
# ### Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# 
# *This function should return a single string value.*

# In[7]:

census_df = pd.read_csv('census.csv')
census_df.head(20)


# In[8]:

def answer_five():
    state_counties = census_df.groupby(['STNAME'])['CTYNAME']
    max_ctn_num = 0
    for i, c in state_counties:
        ctn_num = len(c.values) - 1
        if max_ctn_num < ctn_num:
            max_ctn_num = ctn_num
            cnt = i
    return cnt

answer_five()


# ### Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)?
# 
# *This function should return a list of string values.*

# In[9]:

def answer_six():
    result = {}
    state_counties = census_df.groupby(['STNAME'])
    for i, c in state_counties:
        sorted_c = c.sort_values(by='CENSUS2010POP', ascending=False)
        result[i] = (sorted_c[1:4].sum().CENSUS2010POP)
    temp_df = pd.DataFrame(list(result.items()), columns=['state', 'pop'])
    temp_df = temp_df.sort_values(by='pop', ascending=False)
    return list(temp_df[0:3].state.values)

answer_six()


# ### Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# 
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# 
# *This function should return a single string value.*

# In[10]:

def answer_seven():
    max_diff = 0
    for i, row in census_df.iterrows():
        if row.STNAME != row.CTYNAME:
            pop_list = [row.POPESTIMATE2010, row.POPESTIMATE2011, row.POPESTIMATE2012, row.POPESTIMATE2013, row.POPESTIMATE2014, row.POPESTIMATE2015]
            diff = max(pop_list) - min(pop_list)
            if diff > max_diff:
                max_diff = diff
                ct = row.CTYNAME
    return ct

answer_seven()


# ### Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column. 
# 
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE2014.
# 
# *This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).*

# In[11]:

def answer_eight():
    region1_df = census_df[census_df['REGION'] == 1]
    region2_df = census_df[census_df['REGION'] == 2]
    region_df = pd.concat([region1_df, region2_df])
    count = 0
    temp = []
    my_index = []
    for i, row in region_df.iterrows():
        if row.CTYNAME.find("Washington") == 0:
            if row.POPESTIMATE2015 > row.POPESTIMATE2014:
                temp.append([row.STNAME, row.CTYNAME])
                my_index.append(i)
    my_df = pd.DataFrame(temp, columns=['STNAME', 'CTYNAME'], index=my_index)
    return my_df.sort_index()

answer_eight()

