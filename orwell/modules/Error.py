"""Custom Error handlers for common errors found
in the wild. To be expanded

Classes:
    Error() extending Exception - base error class
    SocketError() extending Error() - socket error handler
    FileError() extending Error() - file I/O error handler

"""
class Error(Exception):
    pass

class SocketError(Error):
    pass

class FileError(Error):
    pass
