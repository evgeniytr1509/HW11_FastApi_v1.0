from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from main import Base, DATABASE_URL

# Создание экземпляра движка SQLAlchemy
engine = create_engine(DATABASE_URL)

# Создание сессии для выполнения запросов к базе данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для создания таблицы в базе данных
def create_table():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Вызов функции для создания таблицы
    create_table()


