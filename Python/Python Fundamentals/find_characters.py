# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def find_characters(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):
        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])
            
    print new_list

find_characters(word_list, char)