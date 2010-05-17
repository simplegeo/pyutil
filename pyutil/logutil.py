# This little file makes it so that we can use "log.msg()" and the contents
# get logged to the Twisted logger if present, else to the Python Standard
# Library logger.

try:
    from twisted.python import log
except ImportError:
    import logging
    class MinimalLogger:
        def msg(self, m):
            logging.log(0, m)
    log = MinimalLogger()

