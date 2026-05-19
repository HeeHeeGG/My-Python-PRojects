from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Password
from schemas import PasswordCreate, PasswordResponse
from encryption import encrypt_password, decrypt_password
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/passwords", response_model=PasswordResponse)
def add_password(entry: PasswordCreate, db: Session = Depends(get_db)):
    encrypted = encrypt_password(entry.password)
    new_entry = Password(
        website=entry.website,
        username=entry.username,
        encrypted_password=encrypted
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return PasswordResponse(
        id=new_entry.id,
        website=new_entry.website,
        username=new_entry.username,
        password=decrypt_password(new_entry.encrypted_password)
    )

@app.get("/passwords", response_model=list[PasswordResponse])
def get_passwords(db: Session = Depends(get_db)):
    entries = db.query(Password).all()
    return [
        PasswordResponse(
            id=e.id,
            website=e.website,
            username=e.username,
            password=decrypt_password(e.encrypted_password)
        )
        for e in entries
    ]

@app.delete("/passwords/{password_id}")
def delete_password(password_id: int, db: Session = Depends(get_db)):
    entry = db.query(Password).filter(Password.id == password_id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Password not found")

    db.delete(entry)
    db.commit()
    return {"message": f"Password for {entry.website} deleted successfully"}





