from sqlalchemy import Integer, String, Column, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Submissions(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lang = Column(String, nullable=False)
    code = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
    execution_time = Column(Integer, nullable=False)  # In milliseconds
    submission_time = Column(DATETIME, nullable=False)

    username = Column(String, ForeignKey("users.username"))
    problem_id = Column(Integer, ForeignKey("problems.problem_id"))
    contest_id = Column(Integer, ForeignKey("contests.contest_id"))

    user = relationship("Users", backref='submissions', foreign_keys=[username])
    problem = relationship("Problems", backref='submissions', foreign_keys=[problem_id])
    contest = relationship("Contests", backref='submissions', foreign_keys=[contest_id])

