import sys
sys.path.append('../module')
from module.Userinfo import *

userInfo = Userinfo()

class Casuserutil:
    
    def verify_login_user(self, user_name, user_password):
        if user_name==userInfo.getUserName() and user_password==userInfo.getUserPassword():
            return 0
        return 1

    def save_user_info(self, user_name, user_password):
        userInfo.setUserName(user_name)
        userInfo.setUserPassword(user_password)