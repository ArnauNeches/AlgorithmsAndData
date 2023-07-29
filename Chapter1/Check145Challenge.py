#Self check 145 Challenge
#Hill climbing algorithm
'''
See if you can improve upon the program in the self check by keeping letters that are correct
and only modifying one character in the best string so far. This is a type of algorithm in the 
class of “hill climbing” algorithms, that is we only keep the result if it is better than the previous
one.
'''
import random

objective = "en un lugar de la mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero adarga antigua rocin flaco y galgo corredor una olla de algo mas vaca que carnero salpicon las mas noches duelos y quebrantos los sabados"
letters_aux = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, "
letters = letters_aux.split(",")

def string_generator(beforestring):
    res = ""
    for i in range(len(objective)):
        if beforestring[i] == objective[i]:
            res = res + beforestring[i]
        else:
            index = random.randint(0,26)
            res = res + letters[index]
    return res

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

def hill_climbing():
    restring = random_string_generator()
    counter = 0
    rescore = 0
    while rescore < 100:
        auxstring = string_generator(restring)
        auxscore = random_string_comparator(auxstring)
        counter += 1
        if rescore < auxscore:
            rescore = auxscore
            restring = auxstring
        print("We are in the cicle number: " + str(counter))
        print("Our actual score is: " + str(rescore))
        print("With the string: " + restring)
        if rescore == 100:
            print("Hill climbing algorithm finished at cicle number " + str(counter) + ". Congratulations!")
        if counter >= 10000001:
            break

hill_climbing()    