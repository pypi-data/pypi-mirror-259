from typing import Optional
from dataclasses import dataclass

@dataclass
class Participant:
    participant_name: str
    participant_location: Optional[str] = None

