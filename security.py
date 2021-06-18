from models.user import UserModel
 
def authenticate(username,password):
    user = UserModel.find_by_username(username)

    if user:
        if(user.password == password):
            return user
        else:
            return None
    else:
        return None            


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_userid(user_id)

    


