"""
    Suppose a rare cancer is 1% of the population. A rare brain disorder affects 5%. 
    With no known correlation, what is the pribability of having 1 and then having both?

    Christina R. 
"""

# Cancer = A, Brain disorder = B
A = 0.01
B = 0.05


# P(patient has both diseases, P(A ∩ B)
has_both = A * B
print(
    f"\nThere is a {A}% chance of having a rare cancer and a {B}% chance of having a rare brain is order."
)
print(f"\nThe chance of having both is: {has_both}")


# P(patient has one of the diseases), P(A ∪ B)
# For the union, we use the inclusion/exclusion: P(A∪B) = P(A)+P(B)−P(A∩B)
union_has_one = A + B - (A * B)
print(f"\nWhile the chance of having one is: {round(union_has_one, 4)}")

""""
    Show that the definition of independence is symmetric,
    P(A|B) = P(A) if and only IF P(B|A) = P(B)

    Further, show that these statements are equivalent to
    P(A ∩ B) = P(A)P(B)
"""

# This is the above problem worked out:

# P(A|B) = P(A)
# P(A∩B)/P(B) = P(A)
# P(A ∩ B) = P(A)P(B)
"""
    (i)Show that the number of triplets of results from tossing a coin 3
    times in which there are k heads is

    (3)
    over
    (k)

    for any k ∈ {0,1,2,3}.

    (ii) Probablility of heads n times

    p(k heads turn up) = (n)
                            p^k(1-p)^n-k
                         (k)       
                     
"""

"""
    What is the probability that the outcome from the first throw is 
    less than the second for a 6-sided die?

    {1st throw = 6, 2nd < 6}
    {1st throw = 5, 2nd < 5}
    {1st throw = 4, 2nd < 4}
    {1st throw = 3, 2nd < 3}
    {1st throw = 2, 2nd < 2}
    {1st throw = 1, 2nd < 1}
"""
from fractions import Fraction

first_throw_6 = (1 / 6) * (5 / 6)
all_throws = (
    (1 / 6) * (5 / 6)
    + (1 / 6) * (4 / 6)
    + (1 / 6) * (3 / 6)
    + (1 / 6) * (2 / 6)
    + (1 / 6) * (1 / 6)
    + (1 / 6) * (0 / 6)
)
fraction_ans = Fraction(all_throws).limit_denominator()

print(
    f"\nIf you have a 6-sided die, the chance that your second roll will be less that your first is {fraction_ans} or {all_throws}.\n"
)

"""
    Suppose a loaded die with probabilities of different outcomes as in the below table is thrown 
    twice. What is the probability that the outcome from the first throw is less than the second?
    1   0.1
    2   0.2
    3   0.25
    4   0.2
    5   0.15
    6   0.1
 P(r1 <r2) = P(r1 =1,r2 >1)
    +P(r1 =2,r2 >2)
    +P(r1 =3,r2 >3) 
    +P(r1 =4,r2 >4)
    +P(r1 =5,r2 >5)
 
= P(r1 =1)P(r2 >1)
    +P(r1 =2)P(r2 >2)
    +P(r1 =3)P(r2 >3) 
    +P(r1 =4)P(r2 >4)
    +P(r1 =5)P(r2 >5)   
"""
# r1 = result on first roll
# r2 = result on second roll

one = 0.1
two = 0.2
three = 0.25
four = 0.2
five = 0.15
six = 0.1
print(
    f"The loaded die percents:\none, {one}\ntwo, {two}\nthree, {three}\nfour, {four}\nfive, {five}\nsix, {six}\n"
)


# r1 < r2
one_roll = two + three + four + five + six
two_roll = three + four + five + six
three_roll = four + five + six
four_roll = five + six
five_roll = six
print(f"\nFirst roll is greater than 1 is equal to {one_roll} percent.")
print(f"First roll is greater than 2 is equal to {two_roll} percent.")
print(f"First roll is greater than 3 is equal to {three_roll} percent.")
print(f"First roll is greater than 4 is equal to {four_roll} percent.")
print(f"First roll is greater than 5 is equal to {five_roll} percent.")

total_chance = (
    one * one_roll
    + two * two_roll
    + three * three_roll
    + four * four_roll
    + five * five_roll
)

print(
    f"The total chance of your first roll (unfair die) will be less than the second is {total_chance} percent."
)


""" 
  If the probablity of having a blonde child is 1/3 and there are 4 children in the a family, 
  what is the chance 2 will be blondes?

  Half of 4 kids being blonde if chance is 1/3 for each

"""
# complement of 2 is at least one.
# not being blonde is 2/3

# no blondes
no_blondes = (2 / 3) ** 4
print("No blondes: ", no_blondes)

one_blonde = (1 / 3) ** 4
exactly_one_blonde_child = 4 * (1 / 3) * ((2 / 3) ** 3)
print("One blonde child :", one_blonde)
print("Exactly one blonde child: ", exactly_one_blonde_child)

# P(at least 2 blonde children) = 1-P(at most 1 blonde)
two_blondes_out_of_four = 1 - no_blondes - exactly_one_blonde_child
print(
    "The chance of having 2 blondes out of four children is: ", two_blondes_out_of_four
)
