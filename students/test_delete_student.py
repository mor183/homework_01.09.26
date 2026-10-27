import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_student import Base, Student

DB_PASSWORD = "ugefer92"
DB_URL_BASE = "postgresql+psycopg2://postgres:{password}@localhost:5432/01"

def test_delete_student_entity():
    safe_password = quote(DB_PASSWORD, safe='')
    db_url = DB_URL_BASE.format(password=safe_password)

    engine = create_engine(db_url, echo=False)

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    student_id = None 

    try:
        new_student = Student(
            name="Anna Smirnova",
            group_name="CS-2024"
        )
        session.add(new_student)
        session.commit()
        session.refresh(new_student)

        student_id = new_student.id
        assert student_id is not None, "Не удалось получить ID созданного студента"

        existing = session.query(Student).filter_by(id=student_id).first()
        assert existing is not None
        assert existing.name == "Anna Smirnova"

        deleted_count = session.query(Student).filter_by(id=student_id).delete()
        session.commit()

        assert deleted_count == 1, f"Ожидалось удалить 1 строку, но удалено: {deleted_count}"

        after_delete = session.query(Student).filter_by(id=student_id).first()
        assert after_delete is None, "Студент всё ещё присутствует в базе после удаления"

        by_name = session.query(Student).filter_by(name="Anna Smirnova").first()
        assert by_name is None, "Студент найден по имени, хотя должен быть удалён"

    except Exception as e:
        session.rollback()
        raise e

    finally:
        if student_id:
            try:
                cleanup_count = session.query(Student).filter_by(id=student_id).delete()
                session.commit()

            except Exception:
                session.rollback()
            finally:
                session.close()
