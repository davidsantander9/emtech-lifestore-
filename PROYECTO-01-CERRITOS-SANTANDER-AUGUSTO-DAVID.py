"""This is a Emtech project"""

user_logged = False
message_error = 'Error' 
message = 'This is a message'

# Users and passwords
users = [
            ['john', 'john-doe'],
            ['jane', 'jane-doe']
        ]

# Ask for credentials
user     = input('Write your user: ')
password = input('Write your password: ')


# Confirm credentials
for u in users:
    if user == u[0] and  password == u[1]:
        message = 'Welcome ' + user
        print(message.center(40, '-'))
        user_logged = True
        break

# Message if credentials are incorrect
if not  user_logged:
    message_error = 'User or password incorrect'
    print(message_error.center(40, '-'))

