"""Custom Error handlers for common errors found
in the wild. To be expanded

Classes:
    Error() extending Exception - base error class
    SocketError() extending Error() - socket error handler
    FileError() extending Error() - file I/O error handler

"""
class BaseError(Exception):
    pass

class SocketError(BaseError):
    pass

class FileError(BaseError):
    pass
