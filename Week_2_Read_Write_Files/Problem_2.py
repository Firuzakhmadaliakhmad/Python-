# Создайте форму регистрации которая спрашивает у пользователя: Логин, Пароль и Фото. 
# Заранее подготовьте фото на компьютере и когда программа спросит ваше фото просто укажите полный путь до места где лежит ваше фото. 
# Программа должна проверить если фото правда существует по такому пути И также это фото с одним из 3 расширений("jpeg", "jpg", "png") то вы сохраняете в файл логин, пароль, путь до фото которое указал пользователь. 
# А самому пользователю вы говорите о том что Регистрация Успешна!


username = input("Username: ")        
password = input("password: ")
image = input("Image path: ")

if image.partition(".")[2] == "jpg" or image.partition(".")[2] == "jpeg" or image.partition(".")[2] == "png":
              
        f = open(image, "rb")    
        newfile = open("imagefile.jpg", "wb")
        
        for i in f:
                newfile.write(i)

        file = open("login.txt", "a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write(" ")
        file.write(image)
        file.write("\n")
        file.close()
        
        print("You registered successfully.")


             