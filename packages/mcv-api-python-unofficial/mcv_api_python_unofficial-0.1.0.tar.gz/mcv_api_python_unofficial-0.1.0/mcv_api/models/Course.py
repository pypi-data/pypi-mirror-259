from dataclasses import dataclass
from typing import List

@dataclass
class Course:
    """
    Course is a dataclass that represents a course
    contain:
    - courseno: str
    - title: str
    """
    courseno: str
    title: str
    
@dataclass
class MyCourse:
    """
    MyCourse is a dataclass that represents a course joined by the user
    comtain:
    - semester: str
    - courses: List[Course]
    """
    semester: str
    courses: List[Course]