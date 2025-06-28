from models import User
from db import session
from passlib.hash import bcrypt

def register(username, email, password):
    existing_user = session.query(User).filter((User.username == username) | (User.email == email)).first()
    
    if existing_user:
        return "❌ Username yoki email band!"
    
    hashed_password = bcrypt.hash(password)
    new_user = User(username=username, email=email, password=hashed_password)
    session.add(new_user)
    session.commit()
    return "✅ Ro‘yxatdan o‘tdingiz!"
