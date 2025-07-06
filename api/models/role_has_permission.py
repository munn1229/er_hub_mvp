from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class RoleHasPermission(Base):
    __tablename__ = 'role_has_permissions'
    __table_args__ = ({
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_unicode_ci'
    },)

    permission_id = Column(
        BIGINT(unsigned=True),
        ForeignKey('permissions.id', ondelete='CASCADE'),
        primary_key=True
    )
    role_id = Column(
        BIGINT(unsigned=True),
        ForeignKey('roles.id', ondelete='CASCADE'),
        primary_key=True
    )