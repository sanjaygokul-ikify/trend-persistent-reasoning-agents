from typing import Dict
import logging
from packages.core.engine import Engine
from packages.core.types import Task, CognitiveFrame
from packages.core.exceptions import EngineError

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, task: Task):
        try:
            self.engine.execute_task(task)
        except EngineError as e:
            logger.error(f"Error executing task {task.id}: {e}")

    def get_task_status(self, task_id: str) -> str:
        return self.engine.get_task_status(task_id)

    def get_result(self, task_id: str) -> Dict:
        return self.engine.get_result(task_id)

    def run(self):
        self.engine.execute_tasks()