from cwstorm.dsl.dag_node import DagNode

# from cwstorm.dsl.cmd import Cmd
import re


class Task(DagNode):
    """task node."""

    ATTRS = {
        "commands": {"type": "list:Cmd"},
        "hardware": {
            "type": "str",
            "validator": re.compile(r"^[a-z0-9_\-\.\s]+$", re.IGNORECASE),
        },
        "env": {"type": "dict"},
        "lifecycle": {"type": "dict", "validator": {"keys": ["minsec", "maxsec"]}},
        "attempts": {"type": "int", "min": 1, "max": 10},
        "initial_state": {
            "type": "str",
            "validator": re.compile(r"^(HOLD|START)$"),
            "default": "HOLD",
        },
        "outputs": {"type": "list:str"},
        "status": {
            "type": "str",
            "validator": re.compile(r"^(WAITING|\d{1,3}|RUNNING|SUCCESS|FAILED)$"),
            "default": "WAITING",
        },
    }

    def __init__(self, name=None):
        """Init the task."""
    
        super().__init__(name)
        self.attempts(1)

        
    def is_original(self, parent=None):
        """True if the parent is the first parent or there are no parents."""
        if not parent:
            return True
        if not self.parents:
            return True
        if self.parents[0] == parent:
            return True
        return False

    def is_reference(self, parent):
        """True if the parent is a parent and not the first parent."""
        return (
            parent
            and self.parents
            and len(self.parents) > 1
            and parent != self.parents[0]
            and parent in self.parents
        )
