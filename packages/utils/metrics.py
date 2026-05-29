class Metrics:
    def __init__(self):
        self.metrics = {}
    
    def add_metric(self, name, value):
        self.metrics[name] = value
    
    def get_metric(self, name):
        return self.metrics.get(name)