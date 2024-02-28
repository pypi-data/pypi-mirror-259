from enum import Enum


class Status(Enum):
    WAIT_CHECK = 0
    CHECKING = 1
    CHECK_ERROR = 2
    CHECKED_WITH_ERRORS = 3
    CHECK_SUCCESS = 4
    FAIL = 5
    AB = 6
    PASS = 7
