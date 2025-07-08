from sqlalchemy import Column, Integer, String, Boolean, Index, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from .base import Base

class ModelHasRole(Base):
    __tablename__ = 'model_has_roles'
    __table_args__ = (
        Index('model_has_roles_model_id_model_type_index', 'model_id', 'model_type'),
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_unicode_ci'
        }
    )

    role_id = Column(
        BIGINT(unsigned=True),
        ForeignKey('roles.id', ondelete='CASCADE'),
        primary_key=True
    )
    model_type = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), primary_key=True)
    model_id = Column(BIGINT(unsigned=True), primary_key=True)