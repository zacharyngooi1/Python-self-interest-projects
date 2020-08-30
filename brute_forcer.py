# Simple Brute Forcer 
import itertools
import time
Possible_letters = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.!@#$%^&*()+=")
password = "hel&a"
time_start = time.perf_counter()
print("Trying all combinations.....")
for x in range(26):
    #Using itertools product to continually change the rightmost index through the string of letters
    possible_passwords = (itertools.product(Possible_letters, repeat=x))
    # Go through each combo with a counter
    for g in possible_passwords:
        password_str = ""
        password_str = password_str.join(g)
        # g is in a list format thus to check, its needed to change it to a string first
        if (password_str == password):
            time_end = time.perf_counter()
            time_taken = time_end - time_start
            print("Password cracked!! Your password is: " + password_str + " taking " + str(time_taken) + " seconds")
            exit()
