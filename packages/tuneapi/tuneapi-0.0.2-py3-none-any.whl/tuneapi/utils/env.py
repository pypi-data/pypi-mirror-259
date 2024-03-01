# Copyright © 2024- Frello Technology Private Limited

import os


class _ENV:
    DISABLE_HOME_DIR = lambda: os.getenv("DISABLE_HOME_DIR", False)

    def __getattr__(self, __name: str):
        return lambda x="": os.getenv(__name, x)


ENV = _ENV()
