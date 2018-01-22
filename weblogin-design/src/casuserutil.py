class Casuserutil:

def verify_login_user(self, user_name, user_password):
    if user_name=='admin' and user_password=='1':
        return 0
    return 1