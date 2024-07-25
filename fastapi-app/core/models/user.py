from sqlalchemy.orm import mapped_column , Mapped

from .base import Base

class User(Base):
    __tablename__ = 'user'
    username: Mapped[str] = mapped_column(unique=True)