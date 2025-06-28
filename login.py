from models import User
from db import session
from passlib.hash import bcrypt

def login():
    username = input("👤 Username: ")
    password = input("🔒 Parol: ")

    user = session.query(User).filter_by(username=username).first()

    if not user:
        print("❌ Bunday foydalanuvchi topilmadi.")
        return

    if bcrypt.verify(password, user.password):
        print(f"✅ Xush kelibsiz, {user.username}!")
    else:
        print("❌ Noto‘g‘ri parol.")
