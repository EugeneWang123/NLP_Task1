import pandas as pd
import numpy as np

#Gets the word list and word frequency list
def sig_wor_fre():
    with open("vocab.txt", 'r', encoding='utf-16-le') as f:
        lines = f.readlines()
        #Top one thousand words in VOCab.txt
        word = []
        #The frequency of the first thousand words in VOCab.txt
        wor_fre = []
        for a in lines[0:1000]:
            word.append(a.split()[0])
            #Make sure i add a number to the Word list, not a string
            wor_fre.append(int(a.split()[-1]))
        # print(wor_fre)
    return word, wor_fre


# sig_wor_fre()
#Synthetic corpus
def corpus(word):
    with open("cleaned.txt", 'r', encoding='utf-16-le') as f:
        #Get text content
        lines = f.readlines()
        #When two words appear in the text at the same time, write them down
        wors_dict = {}
        #Iterate through each row
        for line in lines:
            #Eliminate Spaces on each line
            line = line.strip().split()
            number = 0
            while number in range(len(line)-1):
                #Decide if the first word is in the thousand words
                if line[number] in word:
                    #Decide if the second word is in the thousand words
                    if line[number + 1] in word:
                        #Form a format :(a b)
                        a = line[number] + ' ' + line[number + 1]
                        #The number of occurrences of a qualifying word group is counted cumulatively
                        if a in wors_dict:
                            wors_dict[a] += 1
                        else:
                            wors_dict[a] = 1
                #Let the number go through the range            
                number += 1
        return wors_dict


# word,wor_fre = sig_wor_fre()
# corpus(word)

#The numerator of the formula
def numerator(word, wors_dict):
    #There are multiple lists in a list
    items = []
    #Design word combinations based on the table in the question
    for i in word:
        line_list = []
        for a in word:
            line_list.append((i, a))
        items.append(line_list)
    #Calculation of numerator
    mol = []
    #Iterate through one of multiple lists
    for li in items:
        element = []
        #Iterate over an element in a list
        for a in li:
            #Change the data type of a from a tuple to a string
            b = " ".join(tuple(a))
            if b in wors_dict:
                element.append(wors_dict[b] + 1)
            else:
                element.append(0 + 1)
        mol.append(element)
    # Storing multidimensional arrays
    mol = np.array(mol)
    return mol

#The denominator of the formula
def denominator(word, wor_fre):
    deno = []
    for i in wor_fre:
        a = len(word) + int(i)
        deno.append(a)
    return deno

#Make form
def m_table(word, mol, deno):
    # Every row has the same denominator
    deno = np.array(deno).repeat(1000).reshape(1000, 1000)
    # Divide the numerator by the denominator
    data = np.true_divide(mol, deno)
    # Keep three decimal places
    data = np.round(data, 5)
    # Generate data table
    data_f = pd.DataFrame(data)
    # Rows and columns
    data_f.index = word
    data_f.columns = word
    #Save as a CSV file
    data_f.to_csv('model.csv')


word, wor_fre = sig_wor_fre()
wors_dict = corpus(word)
mol = numerator(word, wors_dict)
deno = denominator(word, wor_fre)
m_table(word, mol, deno)
