from register import register
from login import login

def menu():
    while True:
        print("1. Ro‘yxatdan o‘tish")
        print("2. Tizimga kirish")
        print("0. Chiqish")
        tanlov = input("Tanlang (1/2/0): ")

        if tanlov == "1":
            register()
        elif tanlov == "2":
            login()
        elif tanlov == "0":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❗ Noto‘g‘ri tanlov, qayta urinib ko‘ring.\n")

if __name__ == "__main__":
    menu()
