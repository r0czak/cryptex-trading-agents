class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self):
        """
        This method should be overridden by the concrete agent implementations.
        """
        raise NotImplementedError("Subclasses must implement the run method") 