from enum import Enum


class TaskState(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    TODO = "TODO"