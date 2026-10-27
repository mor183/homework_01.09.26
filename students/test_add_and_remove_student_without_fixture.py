import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from models_student import Base, Student

DB_CONFIG = {
    "username": "postgres",
    "password": "ugefer92",
    "host": "localhost",
    "port": 5432,
    "database": "01"
}

def test_add_and_remove_student_without_fixtures():
    safe_password = quote(DB_CONFIG["password"], safe='')
    
    url = (
        f"postgresql+psycopg2://"
        f"{DB_CONFIG['username']}:{safe_password}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )

    engine = create_engine(url, echo=False)

    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.all()
    except Exception as e:
        pytest.fail(f"Не удалось подключиться к базе данных. Проверьте: 1) Запущен ли PostgreSQL, "
                    f"2) Существует ли база 'mydatabase', 3) Верны ли логин/пароль. Ошибка: {e}")

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = SessionLocal()

    try:
        new_student = Student(name="Ivan Ivanov", group_name="MATH-2024")
        session.add(new_student)
        session.commit()
        session.refresh(new_student)

        student_id = new_student.id
        assert student_id is not None

        fetched = session.query(Student).filter_by(id=student_id).first()
        assert fetched is not None
        assert fetched.name == "Ivan Ivanov"

        deleted_count = session.query(Student).filter_by(id=student_id).delete()
        session.commit()
        assert deleted_count == 1

        after_delete = session.query(Student).filter_by(id=student_id).first()
        assert after_delete is None

    finally:
        session.close()