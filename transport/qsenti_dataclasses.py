from dataclasses import dataclass, field
import numpy as np
import datetime
from typing import TypedDict, Literal
 
@dataclass(slots=True)
class NormalCacheEntry(TypedDict):
    datetime: datetime.date # '2026-06-25T12:30:00.000Z' # From InteractionOutput.sensory.datetime

@dataclass(slots=True)
class NormalCacheStore(TypedDict):
    store: list[NormalCacheEntry]

@dataclass(slots=True)
class QuantumCacheEntry(TypedDict):
    pass

@dataclass(slots=True)
class QuantumCacheStore(TypedDict):
    pass