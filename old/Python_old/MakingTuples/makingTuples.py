# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value.

my_dictionary = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makeTuples(my_dictionary):
    new_list = []
    for key, value in my_dictionary.iteritems():
        new_list.append((key, value))
    print new_list

makeTuples(my_dictionary)

