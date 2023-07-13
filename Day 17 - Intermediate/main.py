class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user was created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Vasya Petrov")
print(f"User {user_1}: id = {user_1.id}, name = {user_1.username}, followers/following = {user_1.followers}/{user_1.following}")
user_2 = User("002", "Anna Herman")
print(f"User {user_2}: id = {user_2.id}, name = {user_2.username}, followers/following = {user_2.followers}/{user_2.following}")
user_1.follow(user_2)
print(f"User {user_1}: id = {user_1.id}, name = {user_1.username}, followers/following = {user_1.followers}/{user_1.following}")
print(f"User {user_2}: id = {user_2.id}, name = {user_2.username}, followers/following = {user_2.followers}/{user_2.following}")