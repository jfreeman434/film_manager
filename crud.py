from sqlalchemy.orm import Session

import models, schemas


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(login=user.login, password=fake_hashed_password, age=user.age, admin=user.admin)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
