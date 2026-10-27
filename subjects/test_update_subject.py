import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_subjects import Base, Subject

DB_PASSWORD = "ugefer92"
DB_URL_BASE = "postgresql+psycopg2://postgres:{password}@localhost:5432/01"

def test_update_subject_entity():
    safe_password = quote(DB_PASSWORD, safe='')
    db_url = DB_URL_BASE.format(password=safe_password)

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    subject_id = None

    try:
        original_subject = Subject(
            name="Linear Algebra",
            code="MATH-101"
        )
        session.add(original_subject)
        session.commit()
        session.refresh(original_subject)

        subject_id = original_subject.id

        subject_to_update = session.query(Subject).filter_by(id=subject_id).first()
        subject_to_update.name = "Advanced Linear Algebra"
        subject_to_update.code = "MATH-301"
        session.commit()

        updated = session.query(Subject).filter_by(id=subject_id).first()
        assert updated is not None
        assert updated.name == "Advanced Linear Algebra"
        assert updated.code == "MATH-301"

        old_check = session.query(Subject).filter(
            Subject.id == subject_id,
            Subject.name == "Linear Algebra"
        ).first()
        assert old_check is None, "Старое имя всё ещё присутствует для этого ID"

    except Exception as e:
        session.rollback()
        raise e

    finally:
        if subject_id:
            try:
                session.query(Subject).filter_by(id=subject_id).delete()
                session.commit()
            except Exception:
                session.rollback()
            finally:
                session.close()
