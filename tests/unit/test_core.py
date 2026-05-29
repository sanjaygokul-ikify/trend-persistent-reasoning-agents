import unittest
from packages.core import Engine, MemoryStore, AgentPool, Task
from packages.utils import logging

class TestCore(unittest.TestCase):
    def test_engine_init(self):
        engine = Engine(MemoryStore(id='memory', data={}), AgentPool(id='agents', agents=[]))
        self.assertIsNotNone(engine.memory_store)
        self.assertIsNotNone(engine.agent_pool)

    def test_add_task(self):
        engine = Engine(MemoryStore(id='memory', data={}), AgentPool(id='agents', agents=[]))
        task = Task(id='task-1', cognitive_frame_id='frame-1', status='pending')
        engine.add_task(task)
        self.assertEqual(len(engine.task_queue), 1)

    def test_get_task_status(self):
        engine = Engine(MemoryStore(id='memory', data={}), AgentPool(id='agents', agents=[]))
        task = Task(id='task-1', cognitive_frame_id='frame-1', status='pending')
        engine.memory_store.store_task(task)
        self.assertEqual(engine.get_task_status(task.id), task.status)

    def test_get_result(self):
        engine = Engine(MemoryStore(id='memory', data={}), AgentPool(id='agents', agents=[]))
        result = {'data': 'result'}
        engine.memory_store.store_result('task-1', result)
        self.assertEqual(engine.get_result('task-1'), result)