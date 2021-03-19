class User:
    """Representation of a user."""
    def __init__(self, first_name, last_name, bio):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.bio = bio

    def describe_user(self):
        description = f"\nHi! My name is {self.first_name} {self.last_name}, and {self.bio}"
        return description

    def greet_user(self):
        greeting = f"\nHi {self.first_name} {self.last_name}"
        return greeting

user_0 = User('miley', 'chen', 'I love Python!')
print(user_0.describe_user())

class Admin(User):
    """Representation of an Admin."""
    def __init__(self, first_name, last_name, bio, privileges):
        super().__init__(first_name, last_name, bio)
        self.privileges = privileges

    def show_privileges(self):
        return(f"\nThis admin can: {self.privileges}")

    def ban_user(self):
        if 'ban' in self.privileges:
            print(f"\n{self.first_name} {self.last_name} wants to ban a user")
            first_name_user = input("first name of user:")
            last_name_user = input("last name of user:")
            return(f"banning {first_name_user} {last_name_user}")
 
admin_0 = Admin('deadly', 'dragon', "I'm a really scary dragon!", ['ban', 'delete post', 'add post'])
print(admin_0.describe_user())
print(admin_0.show_privileges())
print(admin_0.ban_user())
