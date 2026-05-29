from typing import Dict, List
import dataclasses

@dataclasses.dataclass
class CognitiveFrame:
    id: str
    context: Dict

@dataclasses.dataclass
class MemoryStore:
    id: str
    data: Dict

@dataclasses.dataclass
class AgentPool:
    id: str
    agents: List

@dataclasses.dataclass
class Task:
    id: str
    cognitive_frame_id: str
    status: str

@dataclasses.dataclass
class Result:
    id: str
    data: Dict