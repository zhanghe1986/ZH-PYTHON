class Userinfo:

    userName = ''
    userPassword = ''
    userEmail = ''

    def setUserName(self, user_name):
        self.userName = user_name

    def setUserPassword(self, user_password):
        self.userPassword = user_password

    def setUserEmail(self, user_email):
        self.userEmail = user_email

    def getUserName(self):
        return self.userName

    def getUserPassword(self):
        return self.userPassword

    def getUserEmail(self):
        return self.userEmail