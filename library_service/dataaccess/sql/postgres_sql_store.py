from typing import Optional

from sqlalchemy import Column, String, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()


# Demo of how to create data sqlalchemy data model
class File(Base):
    __tablename__ = "Files"

    user = Column(String, primary_key=True, index=True)
    filename = Column(String, primary_key=True, index=True)

    def __str__(self) -> str:
        return f"File[user={self.user}, filename={self.filename}]"


class PostgresStore:

    # Hardcoded connection string for demo
    SQLALCHEMY_DATABASE_URL = (
        "postgresql://library-service:password@localhost:5432/library-service"
    )

    user: str
    password: str
    host: str
    port: int
    database: str
    connection_string: str
    engine: Engine
    session_maker: sessionmaker

    def __init__(self, user, password, host, port, database) -> None:
        connection_string= "postgresql://"+user+":"+password+"@"+host+":"+port+"/"+database
        self.engine = create_engine(PostgresStore.connection_string)
        self.session_maker = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def save_file(self, user: str, file: str):
        session: Session = self.session_maker()
        if session.query(File).filter_by(user=user).first() is None:
            f = File(user=user, filename=file)
            session.add(f)
            session.commit()
        session.close()

    def delete_file(self, user: str, file: str):
        # TODO: implement method
        raise NotImplementedError("TODO: implement method")

    def load_file(self, user: str, file: str) -> Optional[File]:
        session: Session = self.session_maker()
        q = session.query(File).filter_by(user=user, filename=file).first()
        session.close()
        return q
        