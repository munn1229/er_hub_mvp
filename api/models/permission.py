from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class Permission(Base):
    __tablename__ = 'permissions'
    __table_args__ = (
        UniqueConstraint('name', 'guard_name', name='permissions_name_guard_name_unique'),
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_unicode_ci'
        }
    )

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
    guard_name = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
