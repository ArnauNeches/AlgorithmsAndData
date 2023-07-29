#Self check 1.4.4

'''
Modify this code:

word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)
'''

#Modify the code so it doesn´t repeat letters:
word_list = ['cat','dog','rabbit']
letter_list1 = [ ]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list1:
            letter_list1.append(a_letter)
print(letter_list1)

#Redo the code with list comprehension:
letter_list2 = [a_letter for a_word in word_list for a_letter in a_word]
print(letter_list2)
