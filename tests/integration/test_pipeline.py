import unittest
from packages.core import Engine
from packages.utils import logging

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        # Create engine instance
        engine = Engine(MemoryStore(id='memory', data={}), AgentPool(id='agents', agents=[]))
        
        # Create task instance
        task = Task(id='task-1', cognitive_frame_id='frame-1', status='pending')
        
        # Add task to engine
        engine.add_task(task)
        
        # Execute tasks
        engine.execute_tasks()
        
        # Get task status
        task_status = engine.get_task_status(task.id)
        self.assertEqual(task_status, 'completed')