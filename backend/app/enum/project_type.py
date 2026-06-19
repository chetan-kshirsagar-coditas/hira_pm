from enum import Enum

class ProjectType(str, Enum):
    STRATEGIC = "STRATEGIC"
    COMPLIANCE = "COMPLIANCE"
    OPERATIONAL = "OPERATIONAL"
    OTHER = "OTHER"