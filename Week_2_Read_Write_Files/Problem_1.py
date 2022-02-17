# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. 
# Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir. В итоге у вас на рабочем столе должен появиться файл directories.txt. 
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt. Создайте файл users.txt. 
# Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.

def checking(username, password):

    if login(username, password):
        print("Username is already taken.")
        username = input("Username: ")
        password = input("Password: ")
        checking(username, password)
    else:
        file = open("login.txt", "a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write("\n")
        file.close()

        print("Your signed up successfully!!\t Please Log in now\n")
        
        return True


def login(username, password):

    for line in open("login.txt", "r").readlines():
        login_infor = line.split()

        if username == login_infor[0] and password == login_infor[1]:
            return True
        return False


ask = int(input("Pleae type '1' to login , and '2' to sign up....\n\t"))
username = input("Username: ")
password = input("Password: ")
recovery = 0

while 1:
    if ask == 1:
        if login(username, password):
            print("You are logged in!!")
            break
        else:
            if recovery == 3:
                print("Please contact the administrator")
                break

            print("Incorrect username or password.")
            recovery += 1

            username = input("Username: ")
            password = input("Password: ")
            
            if login(username, password):
                print("You are logged in!!")
                break
    else:
        if checking(username, password):
            break