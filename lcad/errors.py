"""
Contains the exceptions of the application
"""


class WipError(NotImplementedError):
    """Raised when work is in progress"""


class UnknownFileFormat(Exception):
    """Raised when the file format is not known"""


class DataInputError(Exception):
    """Raised when the data cannot be outputted"""


class DataOutputError(Exception):
    """Raised when the data cannot be outputted"""
