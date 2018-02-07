# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(lst):
    for i in range(0, len(x)):
        print "*" * x[i]

draw_stars(x)

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def stars_strings(lst):
    for i in range(0, len(x)):
        if type(x[i]) == int:
            print "*" * x[i]
        else:
            str_length = len(x[i])
            lower_case = x[i].lower()
            first_letter = lower_case[:1]
            print first_letter * str_length

stars_strings(x)