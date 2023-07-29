#Self check 1.4.5

'''
Here is a self check that really covers everything so far. You may have heard of the infinite
monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter
keyboard for an infinite amount of time will almost surely type a given text, such as the complete
works of William Shakespeare. Well, suppose we replace a monkey with a Python function.
How long do you think it would take for a Python function to generate just one sentence
of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
You are not going to want to run this one in the browser, so fire up your favorite Python IDE. The
way we will simulate this is to write a function that generates a string that is 28 characters long
by choosing random letters from the 26 letters in the alphabet plus the space. We will write
another function that will score each generated string by comparing the randomly generated
string to the goal.
A third function will repeatedly call generate and score, then if 100% of the letters are correct
we are done. If the letters are not correct then we will generate a whole new string. To make
it easier to follow your program’s progress this third function should print out the best string
generated so far and its score every 1000 tries.
'''

import random

objective = "arnau"
letters_aux = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, "
letters = letters_aux.split(",")

def random_string_generator():
    random_string = ""
    counter = 0
    while counter <= len(objective)-1:
        index = random.randint(0,26)
        random_string = random_string + letters[index]
        counter += 1
    return random_string

def random_string_comparator(ranstring):
    same = 0
    for i in range(len(objective)):
        if objective[i] == ranstring[i]:
            same += 1
    score = same/len(objective)*100
    return score

def monkey_function():
    restring = ""
    counter = 0
    rescore = 0
    while rescore < 100:
        auxstring = random_string_generator()
        auxscore = random_string_comparator(auxstring)
        counter += 1
        if rescore <= auxscore:
            rescore = auxscore
            restring = auxstring
        if counter % 10000 == 0:
            print("We are in the cicle number: " + str(counter))
            print("The highest score we have achieved is: " + str(rescore))
            print("The string was: " + restring)
        if rescore == 100:
            print("Monkey function finished at cicle number " + str(counter) + ". Congratulations!")
        if counter >= 10000001:
            break

monkey_function()
