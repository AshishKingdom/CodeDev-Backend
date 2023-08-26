from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.session import Base, engine


class Problems(Base):
    __tablename__ = "problems"

    problem_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contest_id = Column(Integer, ForeignKey('contests.contest_id'))
    problem_name = Column(String, nullable=False)
    problem_desc = Column(String, nullable=False)
    sample_input = Column(String, nullable=False)
    sample_output = Column(String, nullable=False)
    sample_explanation = Column(String, nullable=False)
    input_format = Column(String, nullable=False)
    output_format = Column(String, nullable=False)
    constraints = Column(String, nullable=False)
    memory_limit = Column(Integer, nullable=False)  # In MB
    time_limit = Column(Integer, nullable=False)  # In milliseconds
    test_input = Column(Text, nullable=False)
    test_output = Column(Text, nullable=False)

    contest = relationship("Contests", backref='problem', foreign_keys=[contest_id])
    # submissions = relationship("Submissions", back_populates='problem')


