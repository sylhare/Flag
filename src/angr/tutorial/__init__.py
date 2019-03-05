import logging

# Show the loggers
for key in logging.Logger.manager.loggerDict:
    print(key)

# Change Logging level in cle ( loads binaries and their associated libraries)
logging.getLogger('cle').setLevel(logging.ERROR)

# Change Logging level in angr
logger = logging.getLogger('angr')
logger.propagate = True  # Propagate to console
logger.disabled = False  # Is Enable
logger.setLevel(logging.WARNING)  # Will show logs starting at warning level (default)
