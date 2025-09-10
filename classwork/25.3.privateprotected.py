class Login:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private
        self._otp = 1234  # protected

    # Getter for private password
    def getpassword(self):
        return self.__password

    # Setter for private password
    def updatePassword(self, new_pwd):
        self.__password = new_pwd

    # OTP getter
    @property
    def publicotp(self):
        return self._otp

    # OTP setter
    @publicotp.setter
    def publicotp(self, value):
        self._otp = value


# Create object
mounika = Login("mounika", "mouni@123")

# Public variable
print("#public")
print("Username:", mounika.username)

# Private variable
print("\n#private")
print("Password:", mounika.getpassword())
# Protected variable via property
print("\n#protected")
print("OTP:", mounika.publicotp)

# Updating public
mounika.username = "_mounika_"
print("\nUpdated username:", mounika.username)

# Updating private
mounika.updatePassword("mouni@456")
print("Updated password:", mounika.getpassword())

# Updating protected via property
mounika.publicotp = 1111
print("Updated OTP:", mounika.publicotp)