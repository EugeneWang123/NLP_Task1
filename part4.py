import pandas as pd
import numpy as np

# Generate Statement
def input_inter():
    #The input sentence
    a = input('Please enter a sentence:')
    #Eliminate the space
    a = a.split()
    #Take the last word in the input sentence
    last_a = a[-1]
    with open("model.csv", 'r') as f:
        #Read the file by line
        lines = f.readlines()
        #Get columns in CSV
        line1 = lines[0]
        #Make a list of a thousand words
        line1 = line1.strip().split()
        #print(lines)
        #Iterate through the second line of reading
        for line in lines[1:]:
            #print(lines[1][0])
            #Slicing the read rows and converting them to the List data type
            line = line.strip().split()
            #When the last word in the input sentence is the same as the first word traversed to each line
            if line[0] == last_a:
                #print(lis_line[0])
                #Iterates through the maximum value of the row read, starting with the second element, 
                #and returns the index value of that maximum value
                max_index = line.index(max(line[1:]))
                #With the index value obtained, go to the previous word list to find the corresponding word
                col_word = line1[max_index]
                print(col_word)
            else:
                pass


input_inter()