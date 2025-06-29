from userr import users

def login():
    print("\n🔐 Tizimga kirish")

    username = input("👤 Username: ")
    password = input("🔑 Parol: ")  # bu yerda parol ko‘rinadi

    for user in users:
        if user['username'] == username:
            if user['password'] == "********":
                print(f"✅ Xush kelibsiz, {username}!\n")
                return
            else:
                print("❌ Parol noto‘g‘ri!\n")
                return

    print("❌ Bunday foydalanuvchi topilmadi.\n")
