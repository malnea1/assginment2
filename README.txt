

1) Create a new user:
 >>adduser towson

2) Give the user a password that is in the dictionary for example "dubai"

3) use this command to run the program:
 >>python assignment2.py towson /etc/shadow
note: you should be root


*If the user exists and has a password, but the password is not in the dictionary, the program will give " no password in dictionary"

*If the specified user does not exist, the program will give an error " user not found"

If the user exists, but does not have a password, the program will give n error " no password"

