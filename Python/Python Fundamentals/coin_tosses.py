# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
import random

def coin_toss(flip):
    total_heads = 0
    total_tails = 0
    print "Starting the program..."

    for i in range(1,flip):
        random_num = random.random()
        num_rounded = round(random_num)

        if num_rounded == 1:
            total_heads += 1
            print "Attempt #{}: Throwing a coin and it's...heads! Got {} heads(s) so far and {} tail(s) so far".format(i, total_heads, total_tails)

        else:
            total_tails += 1
            print "Attempt #{}: Throwing a coin and it's...tails! Got {} heads(s) so far and {} tail(s) so far".format(i, total_heads, total_tails)
            
    print "Ending the program, thank you!"

coin_toss(5001)