import os

def filename():
    # Determine the absolute path of the file
    path = 'C:/Users/王思源/Documents/Python Scripts/dataset/'
    f_list = os.listdir(path)
    for i in f_list:
        # print(i)
        # Separate the filename from the extension, and select only the file with the suffix TXT
        if os.path.splitext(i)[1] == '.txt':
            # Open and read the file
            fp = open(path + i, 'r+', encoding='utf-16le')
            lines = fp.readlines()
            # Iterate through the contents of the file
            line1 = []
            for line in lines:
                start = line.find('<')
                end = line.find('>')
                #When a sentence has "<" and ">"not taking
                if line.isalnum() or (start == -1 and end == -1):
                    #To eliminate the indentation
                    line = line.strip()
                    line1.append(line)
            remove_chara(line1)
            # print(line)
            fp.close()

#Remove special punctuation marks
def remove_chara(lines):
    for line in lines:
        #When traversing characters other than letters and Spaces, replace them
        if line.isalpha() == False or line.isspace() == False:
            #Replace all symbols with Spaces
            line = line.replace(',', '').replace(';', '').replace(':', '').replace('.', '').replace("'", "").replace(
                '!', '').replace('—', '').replace('?', '')
            fp1 = open('cleaned.txt', 'a+', encoding='utf-16le')
            #Write a document, read a line, clean a line, and then write a line
            fp1.writelines(line + '\n')
            fp1.close()

filename()

