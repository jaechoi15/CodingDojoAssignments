# Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.
# Your first function will take in two lists containing some strings.
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Grace", "Jae"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "Sloth", "Cheetah"]

def make_dict(list1, list2):
    combined_list = zip(list1, list2) # Combine the two lists that are passed into the make_dict function
    new_dictionary = dict(combined_list) # Create a dictionary using the combined lists
    print "New Dictionary:", new_dictionary # Print the new_dictionary

make_dict(name, favorite_animal)