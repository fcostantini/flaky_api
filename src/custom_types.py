from dataclasses import dataclass
from typing import Any, Dict

# Gross type simplification of a Json, only used for typing
JSONType = Dict[str, Any]


@dataclass
class House:
    id: int
    address: str
    url: str
