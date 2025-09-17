import sys
if __name__ == "__main__":
    print(sys.path)
    sys.path.append('/Users/aakashagarwal/PyCharm/Resources/DSA/Tree/')

from DSA.Tree.test_cases import users

class UserDatabase:
    """
    A simple in-memory user database that maintains users in sorted order by username.
    Attributes:
        users (list): A list of User objects sorted by username.
    Methods:
        insert(user): Inserts a new user into the database in sorted order.
        find(username): Finds and returns a user by username.
        update(user): Updates an existing user's information.
        list_all(): Returns a list of all users in the database.
    """
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


if __name__ == "__main__":
    # Example usage
    database = UserDatabase() # Create an instance of UserDatabase

    # Insert users into the database in sorted order
    for i in users:
        database.insert(i)

    # Find a user by username
    user = database.find('siddhant')
    print(user)

    # Update a user's information
    from DSA.Tree.user_class import User
    database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
    user = database.find('siddhant')
    print(user)

    # List all users in the database
    database.list_all()
    print(database.list_all())

