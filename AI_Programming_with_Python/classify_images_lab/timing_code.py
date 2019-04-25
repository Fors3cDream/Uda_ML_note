"""
Create by Killer at 2019-04-25 15:12
"""

from time import time, sleep

def main():

    # Sets start time
    start_time = time()

    # sleep somt time
    sleep(5)

    # Sets end time
    end_time = time()

    # Computes overall runtime in seconds
    tot_time = end_time - start_time

    print("\nTotal Elapsed Runtime: ", tot_time, "in seconds.")

    print("\nTotal Elapsed Runtime:", str(int((tot_time/3600))) + " hours:" + str(int((tot_time%3600)/60)) + " minutes:" + str(int((tot_time%3600)%60))+" seconds")


if __name__ == "__main__":
    main()