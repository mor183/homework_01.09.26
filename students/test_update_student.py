import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_student import Base, Student

DB_URL = "postgresql://postgres:ugefer92@localhost:5432/01"

def test_update_student_entity():
    parsed_password = quote("ugefer92", safe='')
    safe_url = f"postgresql+psycopg2://postgres:{parsed_password}@localhost:5432/01"
    
    engine = create_engine(safe_url, echo=False)

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    try:
        original_student = Student(
            name="Ivan Ivanov",
            group_name="MATH-2023"
        )
        session.add(original_student)
        session.commit()
        session.refresh(original_student)

        student_id = original_student.id
        assert student_id is not None, "Студент не был создан (нет ID)"

        assert original_student.name == "Ivan Ivanov"
        assert original_student.group_name == "MATH-2023"

        student_to_update = session.query(Student).filter_by(id=student_id).first()
        
        student_to_update.name = "Ivan Petrov"
        student_to_update.group_name = "PHYS-2024"
        
        session.commit()

        updated_student = session.query(Student).filter_by(id=student_id).first()
        
        assert updated_student is not None
        assert updated_student.name == "Ivan Petrov", f"Имя не обновилось. Было: Ivan Ivanov, стало: {updated_student.name}"
        assert updated_student.group_name == "PHYS-2024", f"Группа не обновилась. Было: MATH-2023, стало: {updated_student.group_name}"

        old_check = session.query(Student).filter(
            Student.id == student_id, 
            Student.name == "Ivan Ivanov"
        ).first()
        assert old_check is None, "Старый вариант имени все еще присутствует для этого ID"

    except Exception as e:
        session.rollback()
        raise e
    
    finally:
        try:
            deleted_count = session.query(Student).filter_by(id=student_id).delete()
            session.commit()
            assert deleted_count == 1, f"Не удалось удалить студента. Удалено строк: {deleted_count}"

            remaining = session.query(Student).filter_by(id=student_id).first()
            assert remaining is None, "Студент остался в базе данных после удаления!"
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()