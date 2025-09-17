class User:
    """
    A class to represent a user with basic attributes and methods.
    Attributes:
        username (str): The unique username of the user.
        name (str): The full name of the user.
        email (str): The email address of the user.
    Methods:
        introduce_yourself(guest_name): Prints a greeting message to the guest.
        __repr__(): Returns a string representation of the user object.
        __str__(): Returns a string representation of the user object (same as __repr__).
    """
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        # print('User created!')

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    # Example usage
    user2 = User('john', 'John Doe', 'john@doe.com')
    print(user2.name)
    print(user2.email, ', ', user2.username)

    user2.introduce_yourself('Jane')
    User.introduce_yourself(user2, 'David') # alternative way


