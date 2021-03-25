def funccreate():
    global newuser
    global newpass
    global nopass
    global nouser
    newuser = input("Create a username: ")
    newpass = input("Create a password:")
    newphone = input("enter your email or phone number: (optional): ")
    Next = input("Write register: ")
    while Next != "register":
        input("Write register: ")

        while newuser == "" and newpass == "":
            newuser = False
            newpass = False
        while newuser == "" and not newpass != "":
            newuser = True
            newpass = False
        while newuser != "" and newpass == "":
            newuser = False
            newpass = True
        while newuser != "" and newpass != "":
            newuser = False
            newpass = False


    if newuser and newpass:
        print("Username and Password true")

    elif newuser and not newpass:
        newpass = input("return and enter a password")
        while newpass == "":
            newpass = input("return and enter a password")

    elif not newuser and newpass:
        newuseruser = input("return and enter a Username")
        while newuser == "":
            newuser = input("return and enter a Username")

    elif not newuser and not newpass:
        newuser = input("return and enter a Username")
        while newuser == "":
            newuser = input("return and enter a Username")
        newpass = input("return and enter a password")
        while newpass == "":
            newpass = input("return and enter a password")

    file = open("userdatabes.txt", "a")
    file.write("username: " + newuser +" "+"password: "+newpass +"\n")
    file.close()

def funclogin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    while username == newuser and password == newpass:
        print("Welcome to Designer.net page")
        break
    while username != newuser and password != newpass:
        print("username or password false")

