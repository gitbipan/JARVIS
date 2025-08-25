import random as ran 
def pwgen():
    chars="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&{*()-_=+[]}|;:'",.<>?/`~"""
    len=int(input("ENTER PASSWORD LENGTH"))
    password=""
    for a in range (len):
        password+=ran.choice(chars)
    return password
while True:
    pwd=pwgen()
    while pwd[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        pwd=pwgen()
    print(pwd)    

     