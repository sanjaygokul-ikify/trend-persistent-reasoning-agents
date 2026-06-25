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

@dataclasses.dataclass
class TaskState:
    status: str
    error: str

    def to_dict(self) -> Dict:
        return {
            'status': self.status,
            'error': self.error
        }

    @staticmethod
    def from_dict(task_state_dict: Dict) -> 'TaskState':
        return TaskState(
            status=task_state_dict['status'],
            error=task_state_dict['error']
        )
