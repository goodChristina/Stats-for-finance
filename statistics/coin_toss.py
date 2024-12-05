"""
I made this to show all the results of a fair coin toss. 
It counts the number of heads and tails for each toss. 

Christina R.
Dec 2024
"""


from itertools import product


def all_outcomes_w_counts(num_tosses):

    outcomes = [
        (outcome, outcome.count("Heads"), outcome.count("Tails"))
        for outcome in product(["Heads", "Tails"], repeat=num_tosses)
    ]
    for outcome, heads_count, tails_count in outcomes:
        print(f"Outcome: {', '.join(outcome)} | H: {heads_count}, T: {tails_count}")


all_outcomes_w_counts(4)
