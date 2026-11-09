from dataclasses import dataclass
import datetime
from typing import TypedDict
 
@dataclass(slots=True)
class NormalCacheEntry(TypedDict):
    datetime: datetime.date 

@dataclass(slots=True)
class NormalCacheStore(TypedDict):
    store: list[NormalCacheEntry]

@dataclass(slots=True)
class QuantumCacheEntry(TypedDict):
    pass

@dataclass(slots=True)
class QuantumCacheStore(TypedDict):
    pass