from nltk.corpus import words
import itertools
import time


#Brute forcing takes a long time so i will try to iterate through common word sin the dictionary and concatente letters and symbols after

Possible_letters = ("1234567890-_.!@#$%^&*()+=")
word_list = words.words()
new = []
query = []
print("Please enter the first letter alphabets of the password to be guessed:")
print("Enter 'done' to start cracking")

while True:
    poss = input()
    if (poss == "done"):
        break
    else:
        query.append(poss)

for finder in word_list:
    for al in query:
        if finder[0] == al: 
            new.append(finder)

password = "blood13#"
string_combi = ""
#236736
print("Cracking.....")
time_start = time.perf_counter()
for x in range(25):
    produced_pass = itertools.product(Possible_letters, repeat=x)
    for b in produced_pass:
        b = list(b)
        for word in new:
            new_list = [word] + b
            if string_combi.join(new_list) == password:
                time_end = time.perf_counter()
                time_taken = time_end - time_start
                print("Password cracked!! Your password is: " + string_combi.join(new_list) + ", taking " + str(time_taken) + " seconds")
                exit()
