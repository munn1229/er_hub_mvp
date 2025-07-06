import os, sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.base import Base
from models.project import Project
from models.model_has_permission import ModelHasPermission
from models.model_as_role import ModelHasRole
from models.password_reset_token import PasswordResetToken
from models.permission import Permission
from models.personal_access_token import PersonalAccessToken
from models.role_has_permission import RoleHasPermission
from models.role import Role
from models.user import User

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
#target_metadata = None
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    dialect = os.getenv("DB_DIALECT", "mysql+pymysql")
    user = os.getenv("DB_USERNAME", "")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    dbname = os.getenv("DB_DATABASE", "er_hub")

    url = f"{dialect}://{user}:{password}@{host}:{port}/{dbname}"
    # url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    dialect = os.getenv("DB_DIALECT", "mysql+pymysql")
    user = os.getenv("DB_USERNAME", "")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    dbname = os.getenv("DB_DATABASE", "er_hub")

    url = f"{dialect}://{user}:{password}@{host}:{port}/{dbname}"

    config.set_main_option("sqlalchemy.url", url)
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
