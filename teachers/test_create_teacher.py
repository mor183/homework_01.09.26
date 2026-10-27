import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_teachers import Base, Teacher

DB_PASSWORD = "ugefer92"
DB_URL_BASE = "postgresql+psycopg2://postgres:{password}@localhost:5432/01"

def test_create_teacher_entity():
    safe_password = quote(DB_PASSWORD, safe='')
    db_url = DB_URL_BASE.format(password=safe_password)

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    teacher_id = None

    try:
        new_teacher = Teacher(
            full_name="Dr. Alice Johnson",
            subject_code="PHYS-201",
            email="alice.johnson@uni.edu"
        )
        session.add(new_teacher)
        session.commit()
        session.refresh(new_teacher)

        teacher_id = new_teacher.id
        assert teacher_id is not None, "Не удалось получить ID созданного преподавателя"

        fetched = session.query(Teacher).filter_by(id=teacher_id).first()
        assert fetched is not None
        assert fetched.full_name == "Dr. Alice Johnson"
        assert fetched.subject_code == "PHYS-201"
        assert fetched.email == "alice.johnson@uni.edu"

    except Exception as e:
        session.rollback()
        raise e

    finally:
        if teacher_id:
            try:
                session.query(Teacher).filter_by(id=teacher_id).delete()
                session.commit()
            except Exception:
                session.rollback()
            finally:
                session.close()
