'''
Problem - I 

sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"
print(verse, "\n")

# split sentence into list of words
sentence_list =  # You will have to fill out the function 
print(sentence_list, '\n')

# convert list to set to get unique words
sentence_set = 
print(sentence_set, '\n')

# print the number of unique words
num_unique = 
print(num_unique, '\n')
'''

# define the sentence
sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drink"

# split sentence into list of words
words_list = sentence.split()

# convert list to set to get unique words
unique_words = set(words_list)

# print the words list and the number of unique words
print("Words list:", words_list)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
