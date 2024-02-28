from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Event:
    event_name: str
    event_timestamp: Optional[float] = None
    event_json: Optional[Dict] = None

    user_id: Optional[str] = None
    session_id: Optional[str] = None

    _exc_value: Optional[Exception] = None
