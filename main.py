from register import register
from login import login
from delete import delete_user
from admin_panel import admin_panel

def menu():
    while True:
        print("\n📋 MENYU:")
        print("1. 📝 Ro‘yxatdan o‘tish")
        print("2. 🔐 Tizimga kirish")
        print("3. 🗑️ Foydalanuvchini o‘chirish")
        print("4. 🛠️ Admin panel")
        print("0. 🚪 Chiqish")

        tanlov = input("Tanlang (1/2/3/4/0): ")

        if tanlov == "1":
            register()
        elif tanlov == "2":
            login()
        elif tanlov == "3":
            delete_user()
        elif tanlov == "4":
            admin_panel()
        elif tanlov == "0":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❗ Noto‘g‘ri tanlov, qaytadan kiriting.\n")

# Dastur boshlanishi
if __name__ == "__main__":
    menu()
