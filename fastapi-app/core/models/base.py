from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase , declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __table_args__(cls):
        return cls.__name__

    id : Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
