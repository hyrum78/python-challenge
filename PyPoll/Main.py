#!/usr/bin/env python
# coding: utf-8

# In[12]:


# open modules

import os
import csv


# In[13]:


# name and set variables
totalvotes = 0
c_name = []
c_list = []
votes = [0, 0, 0, 0]
votes_percent = [0, 0, 0, 0]
winner = []


# In[14]:


# define the path to the file that contains the results of the election

csvpath = os.path.join('.', 'Resources', 'election_data.csv')


# In[15]:


# open the file as a csv file

with open(csvpath, 'r', newline='') as csvfile:

    # read the csv file and store the contents in a variable called csvreader

    csvreader = csv.reader(csvfile, delimiter=',')

    # define the header of the csv file just opened and read and skip it when analysis begins

    csvheader = next(csvreader)

     # loop through entire file to count total votes, add names to the c_name list, and votes per candidate

    for row in csvreader:
        totalvotes += 1
        c_list.append(str(row[2]))
    for row[2] in c_list:
        if row[2] not in c_name:
            c_name.append(row[2])
        if row[2] == c_name[0]:
            votes[0] += 1
        elif row[2] == c_name[1]:
            votes[1] += 1
        elif row[2] == c_name[2]:
            votes[2] += 1
        elif row[2] == c_name[3]:
            votes[3] += 1

    # create a function to calculate the percentage of the total vote for each candidate

    votes_percent[0] = round(100 * (votes[0] / totalvotes), 4)
    votes_percent[1] = round(100 * (votes[1] / totalvotes), 4)
    votes_percent[2] = round(100 * (votes[2] / totalvotes), 4)
    votes_percent[3] = round(100 * (votes[3] / totalvotes), 4)

    # Determine who the winner is
    if votes[0] == max(votes[0], votes[1], votes[2], votes[3]):
       winner = c_name[0]
    elif votes[1] == max(votes[0], votes[1], votes[2], votes[3]):
       winner = c_name[1]
    elif votes[2] == max(votes[0], votes[1], votes[2], votes[3]):
       winner = c_name[2]
    elif votes[3] == max(votes[0], votes[1], votes[2], votes[3]):
       winner = c_name[3]


# In[17]:


# print the report to the terminal screen

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------------")
print(f"{c_name[0]}: {votes_percent[0]}% ({votes[0]})")
print(f"{c_name[1]}: {votes_percent[1]}% ({votes[1]})")
print(f"{c_name[2]}: {votes_percent[2]}% ({votes[2]})")
print(f"{c_name[3]}: {votes_percent[3]}% ({votes[3]})")
print("-----------------------------")
print(f"Winner: {winner}")


# In[19]:


# create a path to a text file in the Output folder

output_path = os.path.join(".", "analysis", "Results.txt")
with open(output_path, 'w', newline='') as text_file:

    # write the report into a text file in the Output folder

    print("Election Results", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Total Votes: {totalvotes}", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"{c_name[0]}: {votes_percent[0]}% ({votes[0]})", file=text_file)
    print(f"{c_name[1]}: {votes_percent[1]}% ({votes[1]})", file=text_file)
    print(f"{c_name[2]}: {votes_percent[2]}% ({votes[2]})", file=text_file)
    print(f"{c_name[3]}: {votes_percent[3]}% ({votes[3]})", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)

    csvfile.close()


# In[ ]:




