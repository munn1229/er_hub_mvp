from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class PasswordResetToken(Base):
    __tablename__ = 'password_reset_tokens'
    __table_args__ = ({
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci'
    },)

    email = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), primary_key=True)
    token = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
