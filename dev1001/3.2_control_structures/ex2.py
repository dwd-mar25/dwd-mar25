# Have variables correct_username = "user123" and correct_password = "password_abc".
correct_username = 'user123'
correct_password = 'password_abc'
# Ask the user for their entered_username and entered_password (using input()).
entered_username = input('Enter your username: ')
entered_password = input('Enter your password: ')
# If entered_username matches correct_username AND entered_password matches correct_password, print "Login successful!".
if entered_username == correct_username and entered_password == correct_password:
    print('Login successful!')
# Else if only the entered_username matches but the password doesn't, print "Incorrect password."
elif entered_username == correct_username and entered_password != correct_password:
    print('Password incorrect')
# Else (if username doesn't match), print "Username not found."
else:
    print('Username not found')

