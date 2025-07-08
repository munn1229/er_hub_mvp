from sqlalchemy import Column, Index
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, TEXT, TIMESTAMP as MySQL_TIMESTAMP
from .base import Base

class PersonalAccessToken(Base):
    __tablename__ = 'personal_access_tokens'
    __table_args__ = (
        Index('personal_access_tokens_tokenable_type_tokenable_id_index', 'tokenable_type', 'tokenable_id'),
        Index('personal_access_tokens_token_unique', 'token', unique=True),
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_unicode_ci'
        }
    )

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    tokenable_type = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
    tokenable_id = Column(BIGINT(unsigned=True), nullable=False)
    name = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), nullable=False)
    token = Column(VARCHAR(64, collation='utf8mb4_unicode_ci'), nullable=False)
    abilities = Column(TEXT(collation='utf8mb4_unicode_ci'), nullable=True)
    last_used_at = Column(MySQL_TIMESTAMP(), nullable=True)
    expires_at = Column(MySQL_TIMESTAMP(), nullable=True)
