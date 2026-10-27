import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_teachers import Base, Teacher

DB_PASSWORD = "ugefer92"
DB_URL_BASE = "postgresql+psycopg2://postgres:{password}@localhost:5432/01"

def test_update_teacher_entity():
    safe_password = quote(DB_PASSWORD, safe='')
    db_url = DB_URL_BASE.format(password=safe_password)

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    teacher_id = None

    try:
        original_teacher = Teacher(
            full_name="Prof. Bob Smith",
            subject_code="MATH-100",
            email="bob.smith@uni.edu"
        )
        session.add(original_teacher)
        session.commit()
        session.refresh(original_teacher)

        teacher_id = original_teacher.id

        teacher_to_update = session.query(Teacher).filter_by(id=teacher_id).first()
        teacher_to_update.full_name = "Prof. Robert Smith Jr."
        teacher_to_update.subject_code = "MATH-200"
        teacher_to_update.email = "robert.smith.jr@uni.edu"
        session.commit()

        updated = session.query(Teacher).filter_by(id=teacher_id).first()
        assert updated is not None
        assert updated.full_name == "Prof. Robert Smith Jr."
        assert updated.subject_code == "MATH-200"
        assert updated.email == "robert.smith.jr@uni.edu"

        old_check = session.query(Teacher).filter(
            Teacher.id == teacher_id,
            Teacher.full_name == "Prof. Bob Smith"
        ).first()
        assert old_check is None, "Старое имя всё ещё присутствует для этого ID"

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
