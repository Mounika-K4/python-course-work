class Instagram:
    def __init__(self, username, password):
        print("Welcome to Instagram")
        self.__bio = ''  # private variable
        self.posts = []
        self.followers = []
        self.following = []
        self.username = username
        self.__password = password  # private variable
        print(f'Hello {self.username} login successful')
    
    # Getter for bio
    @property
    def bio(self):
        return self.__bio
    
    # Setter for bio
    @bio.setter
    def bio(self, upd_bio):
        self.__bio = upd_bio

    # Getter for password
    def showPassword(self):
        return self.__password
    
    # Setter for password
    def updatePassword(self, new_pwd):
        self.__password = new_pwd
        return "Password updated successfully"
        

# Create object
mouni = Instagram('mounika', 'mouni@123')

# Public variables
print("Bio:", mouni.bio)
print('Posts:', mouni.posts)
print('Followers:', mouni.followers)
print('Following:', mouni.following)
print('Username:', mouni.username)

# Modify public variables
mouni.bio = 'sigma'
mouni.posts.append('Pyth.png')
mouni.followers.extend(['hari', 'hema', 'bhavana'])
mouni.following.extend(['ntr', 'rajith', 'kohli'])
mouni.username = 'mani_09'

# After updating
print("Bio:", mouni.bio)
print('Posts:', mouni.posts)
print('Followers:', mouni.followers)
print('Following:', mouni.following)
print('Username:', mouni.username)

# Private variables (through methods)
print("Old Password:", mouni.showPassword())
print(mouni.updatePassword('sada'))
print("New Password:",mouni.showPassword())