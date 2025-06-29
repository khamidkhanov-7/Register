import json
from userr import users

def register():
    print("\n📝 Ro‘yxatdan o‘tish")

    username = input("👤 Username: ")
    email = input("📧 Email: ")
    phone = input("📱 Telefon raqam: ")
    password = input("🔒 Parol: ")

    for user in users:
        if user['username'] == username or user['email'] == email:
            print("❌ Username yoki email band!")
            return

    new_user = {
        "username": username,
        "email": email,
        "phone": phone,
        "password": "********"  # parol ko‘rinmaydi
    }

    users.append(new_user)

    # Faylga yozish (parollar yashiringan)
    with open("userr.py", "w") as f:
        f.write(f"users = {json.dumps(users, indent=4)}")

    print("✅ Ro‘yxatdan o‘tildi!\n")
