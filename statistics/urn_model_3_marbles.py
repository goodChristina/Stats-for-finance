"""
URN MODEL

Suppose the urn has 10 blue marbles, 15 red marbles, 
and 25 green marbles. Suppose the update rule is, 
whatever color is drawn, the marble is returned to the urn, 
and 10 more marbles of the same color are thrown in. 
Calculate the probability of drawing either a blue, red, 
or green marble on the second draw.    

Christina R
"""

# blue, red, green
b = 10
r = 15
g = 25

#the color that is picked that will be added to the total
pick = 10


def draw(x, y, z):
    marble = input(
        "Enter the name of the color of the marble (blue, red or green) you want to know the probability for: "
    ).lower()
    if marble == "blue":
        x = b
        y = g
        z = r
    if marble == "green":
        x = g
        y = b
        z = r
    if marble == "red":
        x = r
        y = b
        z = g
    else:
        print("No such color!")
        # this stops the (g,r,b) from running
        return
    original = x + y + z
    x_original = x / original
    y_original = y / original
    z_original = z / original

    sec_draw_x = (x + pick) / (original + pick)
    sec_draw_y = x / (original + pick)
    sec_draw_z = x / (original + pick)

    chance_x_sec_draw = (
        x_original * sec_draw_x + y_original * sec_draw_y + z_original * sec_draw_z
    )

    print("\nStarting draw: ")
    print(
        f"\nThis is {marble}: ",
        x_original,
        "...and these are the other two: ",
        y_original,
        z_original,
    )
    print(f"\nFirst draw update: ")
    print(sec_draw_x, sec_draw_y, sec_draw_z)
    print(f"\nChance of drawing {marble} in second draw: ")
    print(round(chance_x_sec_draw, 2))


# order doesn't matter
draw(g, r, b)
