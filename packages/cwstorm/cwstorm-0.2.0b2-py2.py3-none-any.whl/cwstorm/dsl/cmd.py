from cwstorm.dsl.node import Node
import re


class Cmd(Node):
    ATTRS = {
        "argv": {
            "type": "list:str",
            "validator": re.compile(r"^[a-zA-Z0-9_@,\-\.\/\s%:]+$", re.IGNORECASE),
        },

    }

    def __init__(self, *args):
        self.argv(*args)
