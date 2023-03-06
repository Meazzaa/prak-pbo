username = str(input("username: "))
password = str(input("password: "))

for i in range(1, 3):
    if username == "informatika" and password == "12345678":
        print("Berhasil login!")
        break
    else:
        print("Username atau password salah coba lagi")
        username = str(input("username: "))
        password = str(input("password: "))
 