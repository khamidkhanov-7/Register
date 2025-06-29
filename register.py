import json
import re
from userr import users

def register():
    print("\n📝 Ro‘yxatdan o‘tish")

    username = input("👤 Username: ")

    # 📧 Email format tekshirish
    while True:
        email = input("📧 Email: ")
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            break
        else:
            print("❌ Email noto‘g‘ri formatda! Masalan: user@example.com")

    # 📱 Telefon raqam format tekshirish
    while True:
        phone = input("📱 Telefon raqam (masalan: +998901234567): ")
        if re.match(r"^\+998\d{9}$", phone):
            break
        else:
            print("❌ Telefon raqam noto‘g‘ri! Masalan: +998901234567")

    password = input("🔒 Parol: ")

    for user in users:
        if user['username'] == username or user['email'] == email:
            print("❌ Username yoki email band!")
            return

    new_user = {
        "username": username,
        "email": email,
        "phone": phone,
        "password": password
    }

    users.append(new_user)

    with open("userr.py", "w") as f:
        f.write(f"users = {json.dumps(users, indent=4)}")

    print("✅ Ro‘yxatdan o‘tildi!\n")
