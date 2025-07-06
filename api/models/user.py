from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('email', name='users_email_unique'),
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_unicode_ci'
        }
    )

    id = Column(CHAR(36, collation='utf8mb4_unicode_ci'), primary_key=True, comment='(DC2Type:guid)')
    name = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
    email = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
    email_verified_at = Column(MySQL_TIMESTAMP(), nullable=True)
    password = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
    remember_token = Column(VARCHAR(100, collation='utf8mb4_unicode_ci'), nullable=True)
    
