def decoration(func):

    def wrapper(*args, **kwargs):
        print(func())
        if func() == True:
            raise Exception('No username defined!')
        elif func() == False:
            raise Exception("No password to change!")
        return ''
    return wrapper

def get_return(func):
    def wrapper():
        if func() == 'account':
            return True
        elif func() == 'password':
            return False
        return 'hello'

    return wrapper

class User:

    @decoration
    @get_return
    def get_account_balance():
        return 'account'

    @decoration
    @get_return
    def change_password():
        return 'password'

user = User()

print(user.change_password())