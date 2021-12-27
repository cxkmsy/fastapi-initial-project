from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="projects")

