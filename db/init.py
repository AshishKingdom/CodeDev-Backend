from db.session import Base, engine

from db.models.user import Users
from db.models.contest import Contests
from db.models.problem import Problems
from db.models.submission import Submissions


def init_database()->None:
    Base.metadata.create_all(engine)

