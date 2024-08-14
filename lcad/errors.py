"""
Contains the exceptions of the application
"""


class WipError(NotImplementedError):
    """Raised when a feature is not yet implemented"""


class UnknownFileFormat(Exception):
    """Raised when the file format is not known"""


class DataInputError(Exception):
    """Raised when the data cannot be loaded"""


class DataOutputError(Exception):
    """Raised when the data cannot be dumped"""
