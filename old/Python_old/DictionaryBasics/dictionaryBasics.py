# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

my_dictionary = {"name": "Jae", "age": "208", "country of birth": "South Korea", "favorite language": "Python"}

def readDictionary(my_dictionary):
    for key, value in my_dictionary.iteritems():
        print "My " + key + " is " + value

readDictionary(my_dictionary)