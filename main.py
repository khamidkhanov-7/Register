from db import Base, engine
from models import User
from register import register
from login import login

Base.metadata.create_all(engine)

while True:
    print("1. Ro‘yxatdan o‘tish")
    print("2. Tizimga kirish")
    print("0. Chiqish")

    tanlov = input("Tanlang (0, 1 yoki 2): ")

    if tanlov == "1":
        username = input("👤 Username (yoki 'orqaga'): ")
        if username.lower() == "orqaga":
            continue

        email = input("📧 Email: ")
        password = input("🔒 Parol: ")
        print(register(username, email, password))
        print()

    elif tanlov == "2":
        login()
        print()

    elif tanlov == "0":
        print("👋 Dasturdan chiqildi.")
        break

    else:
        print("❌ Noto‘g‘ri tanlov.\n")
