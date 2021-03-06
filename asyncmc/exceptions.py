__all__ = ['ClientException', 'ValidationException']


class ClientException(Exception):
    """Raised when the server does something we don't expect."""

    def __init__(self, msg, item=None):
        if item is not None:
            msg = '%s: %r' % (msg, item)
        super(Exception, self).__init__(msg)


class ConnectionDeadError(ClientException):
    """Raised when can not connect to the server"""


class ValidationException(ClientException):
    """Raised when an invalid parameter is passed to a ``Client`` function."""
