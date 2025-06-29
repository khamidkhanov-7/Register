from userr import users

def login():
    print("\n🔐 Tizimga kirish")
    username = input("👤 Username: ")
    password = input("🔑 Parol: ")

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                print(f"✅ Xush kelibsiz, {username}!\n")
                return
            else:
                print("❌ Parol noto‘g‘ri!\n")
                return

    print("❌ Bunday foydalanuvchi topilmadi.\n")
