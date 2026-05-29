import logging
from typing import Dict

class Config:
    def __init__(self, trend_detection_interval: int, reasoning_engine_timeout: int):
        self.trend_detection_interval = trend_detection_interval
        self.reasoning_engine_timeout = reasoning_engine_timeout

    def to_dict(self) -> Dict:
        return {
            'trend_detection_interval': self.trend_detection_interval,
            'reasoning_engine_timeout': self.reasoning_engine_timeout
        }

    @staticmethod
    def from_dict(config_dict: Dict) -> 'Config':
        return Config(
            trend_detection_interval=config_dict['trend_detection_interval'],
            reasoning_engine_timeout=config_dict['reasoning_engine_timeout']
        )

# Initialize the logger
logger = logging.getLogger(__name__)

# Initialize the configuration
config = Config(
    trend_detection_interval=60,
    reasoning_engine_timeout=30
)