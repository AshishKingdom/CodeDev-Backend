from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from schemas.new_contest import ContestData
from schemas.common import SimpleResponse
from core.misc import get_current_userinfo
from db.session import get_db
from db.models.contest import Contests
from db.models.problem import Problems

from datetime import datetime

router = APIRouter()


@router.post("/create_contest", tags=["admin"],)
def create_contest(
        data: ContestData,
        userinfo: dict = Depends(get_current_userinfo),
        db: Session = Depends(get_db)) -> SimpleResponse:
    if userinfo is None or userinfo.get("is_admin") is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please login with admin rights"
        )

    contest = Contests(
        contest_name=data.contest_name,
        description=data.description,
        start=data.start,
        duration=data.duration
    )

    db.add(contest)

    for problems in data.problems:
        db.add(Problems(
            problem_name=problems.problem_name,
            problem_desc=problems.problem_desc,
            sample_input=problems.sample_input,
            sample_output=problems.sample_output,
            sample_explanation=problems.sample_explanation,
            input_format=problems.input_format,
            output_format=problems.output_format,
            constraints=problems.constraints,
            memory_limit=problems.memory_limit,
            time_limit=problems.time_limit,
            test_input=problems.test_input,
            test_output=problems.test_output,
            contest=contest
        ))

    db.commit()
    return SimpleResponse(detail='Contest added successfully!')
