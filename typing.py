from time import *
import random as rd
import paragraphs as pg

def mistake_count(original,user_test):
    word_mistake = 0

    for i in range(len(original)):
        try:
            if original[i] != user_test[i]:
                word_mistake += 1
        except:
            word_mistake += 1
    return word_mistake

def time_calculation(s_time,e_time):
    difference = (e_time - s_time)
    round_difference = round(difference)
    if round_difference > 60:
        minute = round((round_difference/60),2)
        print(f"Total time taken : {minute} minutes")

    elif round_difference <60:
        print(f"Total time taken : {round_difference} seconds")

random_paragraph = rd.choice(pg.list_of_paragraph)
print("\nType this Paragraph : \n",random_paragraph)
print("================ Your time Starts Now ================")
start_time = time()
user_test = input("Start typing : \n")
end_time = time()
time_calculation(start_time,end_time)
print("Total mistakes : ",mistake_count(random_paragraph,user_test))

