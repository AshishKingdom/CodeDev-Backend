from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from db.session import Base


class Contests(Base):
    __tablename__ = "contests"

    contest_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start = Column(Integer, nullable=False)  # Unix epoch time (seconds)
    end = Column(Integer, nullable=False)  # Unix epoch time (seconds)

    # problem = relationship("Problems", back_populates='contest')
    # submissions = relationship("Submissions", back_populates='contest')
