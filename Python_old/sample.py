class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Duke Doodle", "anna@anna.com")
user2 = User("user 2", "anna@anna.com")
print user1.name
print user1.email
print user1.logged
print user2.name
print user2.email
print user2.logged