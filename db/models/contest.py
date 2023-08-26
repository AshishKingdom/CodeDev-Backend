from sqlalchemy import Integer, String, Column, DATETIME
from sqlalchemy.orm import relationship
from db.session import Base


class Contests(Base):
    __tablename__ = "contests"

    contest_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start = Column(DATETIME, nullable=False)
    duration = Column(Integer, nullable=False)

    # problem = relationship("Problems", back_populates='contest')
    # submissions = relationship("Submissions", back_populates='contest')


