from sqlalchemy.orm import relationship
from .er_diagram import ErDiagram
from .model_has_permission import ModelHasPermission
from .model_has_role import ModelHasRole
from .password_reset_token import PasswordResetToken
from .permission import Permission
from .personal_access_token import PersonalAccessToken
from .project import Project
from .role_has_permission import RoleHasPermission
from .role import Role
from .user import User
from .branch import Branch
from .commit import Commit

User.projects = relationship("Project", back_populates="user")
User.er_diagrams = relationship("ErDiagram", back_populates="user")
User.branches = relationship("Branch", back_populates="user")
User.commits = relationship("Commit", back_populates="user")

Project.user = relationship("User", back_populates="projects")
Project.er_diagrams = relationship("ErDiagram", back_populates="project")

ErDiagram.user = relationship("User", back_populates="er_diagrams")
ErDiagram.project = relationship("Project", back_populates="er_diagrams")
ErDiagram.branches = relationship("Branch", back_populates="er_diagram")

Branch.user = relationship("User", back_populates="branches")
Branch.er_diagram = relationship("ErDiagram", back_populates="branches")
Branch.commits = relationship("Commit", back_populates="branch")

Commit.user = relationship("User", back_populates="commits")
Commit.branch = relationship("Branch", back_populates="commits")
