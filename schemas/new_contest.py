from pydantic import BaseModel
from typing import List
from datetime import datetime


class ProblemData(BaseModel):
    """
    Problem Data
    """
    problem_name: str
    problem_desc: str
    sample_input: str
    sample_output: str
    sample_explanation: str
    input_format: str
    output_format: str
    constraints: str
    memory_limit: int
    time_limit: int
    test_input: str
    test_output: str


class ContestData(BaseModel):
    """
    Contest Data : Consisting of contest information along with
    problem details
    """

    contest_name: str
    description: str
    start: int
    duration: int
    problems: List[ProblemData]
