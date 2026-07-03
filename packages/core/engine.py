from typing import Dict, List, Tuple
import logging
from .types import CognitiveFrame, MemoryStore, AgentPool, Task
from .exceptions import EngineError, MemoryAccessError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, memory_store: MemoryStore, agent_pool: AgentPool):
        self.memory_store = memory_store
        self.agent_pool = agent_pool
        self.task_queue = []

    def add_task(self, task: Task):
        self.task_queue.append(task)

    def execute_tasks(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            try:
                self.execute_task(task)
            except EngineError as e:
                logger.error(f"Error executing task {task.id}: {e}")
                task.status = "failed"
                self.memory_store.update_task(task)
            except Exception as e:
                logger.error(f"Unexpected error executing task {task.id}: {e}")
                task.status = "failed"
                self.memory_store.update_task(task)

    def execute_task(self, task: Task):
        # Load cognitive frame from memory store
        cognitive_frame = self.memory_store.load_cognitive_frame(task.cognitive_frame_id)
        if not cognitive_frame:
            raise MemoryAccessError(f"Cognitive frame {task.cognitive_frame_id} not found")

        # Execute task using agent pool
        agent = self.agent_pool.get_available_agent()
        if not agent:
            raise EngineError("No available agents")

        try:
            result = agent.execute_task(task, cognitive_frame)
            self.memory_store.store_result(task.id, result)
            task.status = "completed"
            self.memory_store.update_task(task)
        except Exception as e:
            logger.error(f"Error executing task {task.id}: {e}")
            task.status = "failed"
            self.memory_store.update_task(task)

        # Add timeout handling
        if task.status != 'completed' and task.status != 'failed':
            task.status = 'timed_out'
            self.memory_store.update_task(task)

    def get_task_status(self, task_id: str) -> str:
        task = self.memory_store.get_task(task_id)
        if task:
            return task.status
        return "not_found"

    def get_result(self, task_id: str) -> Dict:
        result = self.memory_store.get_result(task_id)
        if result:
            return result
        return {}

    def get_task(self, task_id: str) -> Task:
        return self.memory_store.get_task(task_id)

    # Added timeout handling for execute_task
    def execute_task_with_timeout(self, task: Task, timeout: int):
        import signal
        def handler(signum, frame):
            raise TimeoutError()
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        try:
            self.execute_task(task)
        except TimeoutError:
            task.status = 'timed_out'
            self.memory_store.update_task(task)
        finally:
            signal.alarm(0)
