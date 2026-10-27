import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_subjects import Base, Subject

DB_PASSWORD = "ugefer92"
DB_URL_BASE = "postgresql+psycopg2://postgres:{password}@localhost:5432/01"

def test_delete_subject_entity():
    safe_password = quote(DB_PASSWORD, safe='')
    db_url = DB_URL_BASE.format(password=safe_password)

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    subject_id = None

    try:
        new_subject = Subject(
            name="Physics Basics",
            code="PHYS-100"
        )
        session.add(new_subject)
        session.commit()
        session.refresh(new_subject)

        subject_id = new_subject.id

        deleted_count = session.query(Subject).filter_by(id=subject_id).delete()
        session.commit()

        assert deleted_count == 1, f"Ожидалось удалить 1 строку, но удалено: {deleted_count}"

        after_delete = session.query(Subject).filter_by(id=subject_id).first()
        assert after_delete is None, "Предмет всё ещё присутствует в базе после удаления"

    except Exception as e:
        session.rollback()
        raise e

    finally:
        if subject_id:
            try:
                cleanup_count = session.query(Subject).filter_by(id=subject_id).delete()
                session.commit()
            except Exception:
                session.rollback()
            finally:
                session.close()
