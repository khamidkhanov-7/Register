import json
from userr import users

def delete_user():
    print("\n🗑️ Foydalanuvchini o‘chirish")

    username = input("👤 Username: ")
    password = input("🔑 Parol: ")

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                users.remove(user)

                with open("userr.py", "w") as f:
                    f.write(f"users = {json.dumps(users, indent=4)}")

                print(f"✅ Foydalanuvchi '{username}' o‘chirildi.\n")
                return
            else:
                print("❌ Parol noto‘g‘ri!")
                return

    print("❌ Bunday foydalanuvchi topilmadi.\n")
