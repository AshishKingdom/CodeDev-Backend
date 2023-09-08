from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.orm import Session
from sqlalchemy import and_, select

from datetime import datetime
import pytz

from db.models.contest import Contests
from db.models.problem import Problems
from db.session import get_db

from schemas.contests import ContestQueryResult, SingleContest, ProblemIDName, ContestProblems

router = APIRouter()


@router.get("/contests", tags=["contest"])
def get_contests(flag: str = "all", db: Session = Depends(get_db)) -> ContestQueryResult:
    flag = flag.lower()

    contest_data = []
    data = None
    curr_time: int = int(datetime.now(pytz.timezone('Asia/Kolkata')).timestamp())
    if flag == "all":
        data = db.execute(select(Contests)).scalars()
    elif flag == "past":
        data = db.execute(select(Contests).where(
            Contests.end < curr_time
        )).scalars()
    elif flag == "future":
        data = db.query(Contests).filter(
            Contests.start > curr_time
        )
    elif flag == "present":
        data = db.query(Contests).filter(and_(
            Contests.start <= curr_time,
            Contests.end >= curr_time
        ))
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="invalid flag passed"
        )

    for p in data:
        contest_data.append(
            SingleContest(
                id=p.contest_id,
                name=p.contest_name,
                description=p.contest_name,
                start=p.start,
                end=p.end
            )
        )
    return ContestQueryResult(contests=contest_data)


@router.get("/contest/{contest_id}", tags=["contest"])
def get_contest_info(contest_id: int, db: Session = Depends(get_db)) -> ContestProblems:
    if contest_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="expected contest id"
        )

    data = db.execute(select(Problems).where(Problems.contest_id==contest_id)).scalars()
    problem_list = []
    for p in data:
        problem_list.append(
            ProblemIDName(id=p.problem_id, name=p.problem_name)
        )

    return ContestProblems(contest_id=contest_id, problems=problem_list)
