from enum import Enum
from typing import List

class SupportedLeagues(str, Enum):
    NBA = "NBA"
    # NBL = "NBL"
    # NFL = "NFL"
    # AFL = "AFL"

    def as_list() -> List[str]:
        return [e.value for e in SupportedLeagues]

