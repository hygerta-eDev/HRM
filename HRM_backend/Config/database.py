import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from fastapi import Body

# DATABASE_URL = "postgresql://postgres:Edev2002+@db/prova1"
DATABASE_URL = "postgresql://postgres:Edev2002+@db:5432/prova3"


# DATABASE_URL = "postgresql://postgres:Edev2002+@localhost/prova1"
# DATABASE_URL = "postgresql://postgres:Edev2002+@localhost/prova10"
# DATABASE_URL = "mysql+pymysql://root:Edev2002+@localhost/test1"

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
    class DummySession:
            def add(self, instance):
                pass
            
            def commit(self):
                pass
            
            def refresh(self, instance):
                pass
            
            def query(self, model):
                return []
        
    return DummySession()