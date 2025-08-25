import random as ran 
while True:
    len=int(input("ENTER PASSWORD LENGTH"))
    def pwgen():
        chars="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&{*()-_=+[]}|;:'",.<>?/`~"""
        password=""
        for a in range (len):
            password+=ran.choice(chars)
        return password

    pwd=pwgen()
    while pwd[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        pwd=pwgen()
    print(pwd)    

    
    