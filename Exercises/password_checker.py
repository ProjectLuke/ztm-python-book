# '*' * 10
#obje
# Pass Checker
# Create an input asking for username
# Create another input asking for password
# At the end want to print something like 
# 	"Password is {password} is {password_length} long"
# Because we don't actually want to display the password
# 	make sure the password is displayed in *******
#Logic behind this
# input_one = "Ask user for a username"
# input_two = "Ask user for a password"

# pass_length = calculate length of password

# print(f"Your user name is : {username} your password {password in asterisk} is {length} long")

def pass_length(x):
    y = len(x)
    return y

def pass_encrypt(x):
    y = '*'* pass_length(x)
    return y
    

print("Login Credentials\n=================")
username_input = input("Username: ")
password_input = input("Password: ")

password_length = pass_length(password_input)

print(f"Username: {username_input}\nPassword: {pass_encrypt(password_input)}\nPassword Length: {pass_length(password_input)} ")
 