class EngineError(Exception):
    pass

class MemoryAccessError(EngineError):
    pass

class AgentError(EngineError):
    pass

class TaskError(EngineError):
    pass