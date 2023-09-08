from pydantic import BaseModel
from typing import List
from datetime import datetime


class SingleContest(BaseModel):
    id: int
    name: str
    description: str
    start: int
    end: int


class ContestQueryResult(BaseModel):
    contests: List[SingleContest]


class ProblemIDName(BaseModel):
    id: int
    name: str


class ContestProblems(BaseModel):
    contest_id: int
    problems: List[ProblemIDName]
