class GlobalMemoryError(Exception):
    """Base error shown to CLI users without a traceback."""


class ValidationError(GlobalMemoryError):
    """Input or document validation failed."""


class NotFoundError(GlobalMemoryError):
    """A requested object does not exist."""


class ImmutableContentError(GlobalMemoryError):
    """An operation would overwrite immutable raw content."""
