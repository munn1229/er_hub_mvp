from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class ModelHasPermission(Base):
    __tablename__ = 'model_has_permissions'
    __table_args__ = (
        Index('model_has_permissions_model_id_model_type_index', 'model_id', 'model_type'),
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_unicode_ci'
        }
    )

    permission_id = Column(
        BIGINT(unsigned=True),
        ForeignKey('permissions.id', ondelete='CASCADE'),
        primary_key=True
    )
    model_type = Column(VARCHAR(255, collation='utf8mb4_unicode_ci'), primary_key=True)
    model_id = Column(BIGINT(unsigned=True), primary_key=True)    
