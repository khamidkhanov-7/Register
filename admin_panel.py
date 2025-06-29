import json
from userr import users

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_panel():
    print("\n🔐 Admin panelga kirish")

    for urinish in range(3):
        username = input("👤 Admin username: ")
        password = input("🔑 Admin parol: ")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            break
        else:
            print("❌ Admin ma'lumotlari noto‘g‘ri!")
            if urinish == 2:
                print("🔒 3 marta noto‘g‘ri urinish! Qayta urinib ko‘ring.\n")
                return

    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. 👥 Barcha foydalanuvchilarni ko‘rish")
        print("2. 🗑️ Foydalanuvchini o‘chirish")
        print("3. 🔒 Foydalanuvchi parolini yangilash")
        print("0. 🚪 Chiqish")

        tanlov = input("Tanlang (1/2/3/0): ")

        if tanlov == "1":
            print("\n📋 Foydalanuvchilar:")
            for i, user in enumerate(users, 1):
                print(f"{i}. {user['username']} | {user['email']} | {user['phone']} | ********")

        elif tanlov == "2":
            uname = input("🗑️ O‘chiriladigan username: ")
            for user in users:
                if user['username'] == uname:
                    users.remove(user)
                    with open("userr.py", "w") as f:
                        f.write(f"users = {json.dumps(users, indent=4)}")
                    print(f"✅ '{uname}' foydalanuvchisi o‘chirildi!")
                    break
            else:
                print("❌ Foydalanuvchi topilmadi!")

        elif tanlov == "3":
            uname = input("🔁 Paroli yangilanadigan username: ")
            for user in users:
                if user['username'] == uname:
                    new_pass = input("🆕 Yangi parol: ")
                    user['password'] = new_pass
                    with open("userr.py", "w") as f:
                        f.write(f"users = {json.dumps(users, indent=4)}")
                    print("✅ Parol yangilandi!")
                    break
            else:
                print("❌ Foydalanuvchi topilmadi!")

        elif tanlov == "0":
            print("👋 Admin paneldan chiqildi.")
            break

        else:
            print("❗ Noto‘g‘ri tanlov.")
