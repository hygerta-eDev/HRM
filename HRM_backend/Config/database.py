import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

# DATABASE_URL = "postgresql://postgres:Edev2002+@localhost/prova1"
DATABASE_URL = "postgresql://postgres:Edev2002+@localhost/prova5"
engine = sql.create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()