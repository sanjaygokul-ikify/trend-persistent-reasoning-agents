import argparse
from packages.core import Engine
from packages.utils import logging

parser = argparse.ArgumentParser(description='Persistent Reasoning Agents CLI')
def main():
    parser.add_argument('--config', help='Path to configuration file')
    args = parser.parse_args()
    
    # Create engine instance
    engine = Engine(memory_store=None, agent_pool=None)
    
    # Start engine
    engine.execute_tasks()

if __name__ == '__main__':
    main()