import matplotlib.pyplot as plt

#Open the file and slice the contents of the file into the List
def read_file():
    with open('cleaned.txt', 'r', encoding='utf-16-le') as f:
        lines = f.readlines()
        word = []
        for line in lines:
            # Remove empty lines
            if line.strip() != "":
                # Convert the word to lowercase
                line = line.lower()
                # Cut the traversal sentence into words according to the space
                a = line.strip().split(' ')
                word.extend(a)
        return word

# Remove duplicate words and keep unique words and count the frequency of words
def word_fre(list1):
    #The key is the word, and the value is the frequency of the word
    wor_num = {}
    #Iterate through the sliced content
    for a in list1:
        #Determines if the traversed character is not a space and it is in the created dictionary
        if a in wor_num and a != ' ':
            wor_num[a] += 1
        else:
            wor_num[a] = 1
    return wor_num

#Gets the word list and word frequency list
def sort(dict):
    new_num = {}
    #Sort the dictionary
    new_num = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # print(new_num)
    #Write the sorted dictionary into the vocab.txt file
    with open('vocab.txt', 'w', encoding='utf-16-le') as f:
        #A key-value pair is a row
        for item in new_num:
            word = item[0]
            number = item[1]
            f.write(str(word) + "   :   " + str(number) + "\n")


# a = read_file()
# print(a)
# b = word_fre(a)
# print(b)
# c = sort(b)
# print c
# sort(word_fre(read_file()))


#Graph of frequency against first 100 words in sorted vocab
def frequence_word():
    with open('vocab.txt', 'r', encoding='utf-16-le') as f:
        word_num = f.readlines()
        # Change the span size
        plt.figure(figsize=(12.8, 12.8))
        #Set the X-axis and Y-axis data
        x = []#X is the list of words
        y = []#Y is the word frequency list
        for a in word_num[0:100]:
            # print(a)
            x.append(a.split()[0])
            # print(x)
            y.append(int(a.split()[-1]))
        # print(x,y)
        # Change the order of the data on the x and Y axes, respectively
        y.reverse()
        x.reverse()
        #Change the color of the bar chart
        plt.bar(x, y, color='rgb')
        # Flip the X-axis words 90 degrees to make the X-axis look clear
        plt.xticks(rotation=90)
        #Set the titles of the x and Y axes
        plt.xlabel("first 100 words")
        plt.ylabel("frequency")
        #Save the diagram
        plt.savefig("first_100_words.png")
        # plt.show()



# frequence_word()


#Graph of words that occur n time against word occurrence
def word_occu():
    with open('vocab.txt', 'r', encoding='utf-16-le') as f:
        word_num = f.readlines()
        #For efficiency, traverse the file data from the bottom
        word_num.reverse()  
        # Set the span size
        plt.figure(figsize=(12.8, 12.8))
        fre_word = {} 
        #
        for a in word_num:
            a = a.split()
            # print(a)
            if int(a[-1]) <= 250:
                a = a[-1]
                if a in fre_word:
                    fre_word[a] += 1
                else:
                    fre_word[a] = 1
                    # print(fre_word)
    #Set the X-axis and Y-axis data
    x = []
    y = []
    for key, value in fre_word.items():
        x.append(str(key))
        y.append(value)
    # print(x,y)
    #Draw the line chart
    plt.plot(x, y)
    plt.xticks(rotation=90)
    # plt.show()
    #Set the titles of the x and Y axes
    plt.xlabel("fre_word")
    plt.ylabel("times_word")
    plt.savefig("word_occurrence.png")
    # print(x)

# word_occu()

#Main program, call function one by one in order
def main():
    list1 = read_file()
    dict = word_fre(list1)
    sort(dict)
    frequence_word()
    word_occu()


if __name__ == '__main__':
    main()
