import itertools
import time


Possible_letters = ("1234567890-_.!@#$%^&*()+=")

print("Please enter word to concatenate to random numbers and symbols:")

poss = input()


password = "blood13"
string_combi = ""


print("Cracking.....")
time_start = time.perf_counter()
for x in range(25):
    produced_pass = itertools.product(Possible_letters, repeat=x)
    for b in produced_pass:
        b = list(b)
        new_list = [poss] + b
        if string_combi.join(new_list) == password:
            time_end = time.perf_counter()
            time_taken = time_end - time_start
            print("Password cracked!! Your password is: " + string_combi.join(new_list) + ", taking " + str(time_taken) + " seconds")
            exit()