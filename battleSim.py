# Import statements for matplotlib
import matplotlib.pyplot as plt
import numpy as np

def sim(fallen, alive):
# sim: Recursive function to calculate the win probability in a battle between
# the fallen and the alive when the individual probability is 0.5. When the
# fallen win, they add 1 to their number while subtracting one from the alive.
# When the alive win, they subtract one from the fallen's number without adding
# to their own.
#
# INPUTS:
#   fallen: Number of soldiers in the fallen army
#   alive: Number of soldiers in the alive army
#
# OUTPUTS:
#   winRate: double value that represents the probaility of the alive winning

    # If there are no fallen left, the alive win
    if fallen < 1:
        return 1.0
    # If there are no alive left, the fallen win
    elif alive < 1:
        return 0.0
    # If there are at least 1 fallen and 1 alive, calculate probaility
    else:
        return (0.5*(sim(fallen-1, alive)) + 0.5*(sim(fallen+1, alive-1)))

def main():
    # TODO: add code to plot results using matplotlib
    print("Not implemented yet...")

# Tells interpreter what to run if script is run
if __name__ == "__main__":
    main()
