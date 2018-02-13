# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

me = {
    "name":"Jae",
    "country of birth":"South Korea",
    "favorite language":"Python",
    "favorite hobby":"snowboarding"
}

def read_dictionary(dict):
    print "My name is {}".format(dict["name"])
    print "My country of birth is {}".format(dict["country of birth"])
    print "My favorite language is {}".format(dict["favorite language"])
    print "My favorite hobby is {}".format(dict["favorite hobby"])

read_dictionary(me)