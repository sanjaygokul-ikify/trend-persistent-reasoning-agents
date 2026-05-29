from packages.core import Engine
from . import config

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine
    
    def start(self):
        self.engine.execute_tasks()