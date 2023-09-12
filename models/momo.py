import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column
from db_engine import Base


class CheckTable(Base):
    __tablename__ = "check_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    just_field: Mapped[str] = mapped_column(sa.String(50))
