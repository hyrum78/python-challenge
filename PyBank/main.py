#!/usr/bin/env python
# coding: utf-8

# In[15]:


# import modules
import os
import csv


# In[44]:


# define variables for magical calculations that probably won't work :(

changevals = []
priorval = float(0)
profits = []
totalpnl = float(0)
countmonths = 0
date_ls = []


# In[45]:


# road to data

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


# In[46]:


with open(csvpath, 'r', newline='') as csvfile:

# read the csv file and store the contents in a variable called csvreader

    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# loop to count months, dates and p&l info

    for value in csvreader:
        countmonths += 1
        
        date_ls.append(str(value[0]))
        profits.append(float(value[1]))

    # list all p&l change

        current_value = value[1]
        change_value = float(current_value) - float(priorval)
        changevals.append(change_value)
        priorval = current_value


# In[47]:


# compute avg change for p&l between months

def average(changevals):
    x = len(changevals)
    total = sum(changevals) - changevals[0]
    avg = total / (x - 1)
    return avg


# In[48]:


# compute avg change using changevals

average_change = round(average(changevals), 2)


# In[49]:


# sum total p&l 

totalpnl = round(sum(profits))


# In[53]:


# line up dates

highest_pnl = round(max(profits))
lowest_pnl = round(min(profits))
highest_index = profits.index(highest_pnl)
lowest_index = profits.index(lowest_pnl)

# print the pretty report  

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {countmonths}")
print(f"Total: ${totalpnl}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_ls[highest_index]} ({highest_pnl})")
print(f"Greatest Decrease in Profits: {date_ls[lowest_index]} ({lowest_pnl})")


# In[54]:


# create output path for Fin_Analysis file

outputpath = os.path.join(".", "analysis", "Fin_Analysis.txt")
with open(outputpath, 'w', newline='') as text_file:

# write the file in analysis folder

    print("Financial Analysis", file=text_file)
    print('-----------------------------', file=text_file)
    print(f"Total Months: {countmonths}", file=text_file)
    print(f"Total: ${totalpnl}", file=text_file)
    print(f"Average Change: ${average_change}", file=text_file)
    print(f"Greatest Increase in Profits: {date_ls[highest_index]} ({highest_pnl})", file=text_file)
    print(f"Greatest Decrease in Profits: {date_ls[lowest_index]} ({lowest_pnl})",file=text_file)

# close file

    csvfile.close()


# In[ ]:





# In[ ]:




