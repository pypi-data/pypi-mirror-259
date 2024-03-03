"""
Exceptions shared across the joes-giant-toolbox package
"""


class MaxRetriesExceededError(Exception):
    """Error raised if have retried too many times"""

    def __init__(self, message):
        super().__init__(message)
