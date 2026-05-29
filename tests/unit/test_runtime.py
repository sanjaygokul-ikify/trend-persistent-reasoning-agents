import unittest
from packages.core import Engine

class TestRuntime(unittest.TestCase):
    def test_runtime(self):
        engine = Engine(MemoryStore(id='memory', data={}), AgentPool(id='agents', agents=[]))
        self.assertIsNotNone(engine)