import logging
import logging.config

# Logging configuration
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "default",
        },
    },
    "loggers": {
        "": {  # root logger
            "level": "INFO",
            "handlers": ["console", "file"],
        },
        "myapp": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },
}

logging.config.dictConfig(log_config)
logger = logging.getLogger("app")

# logs.py

# import logging
# import logging.config

# # Basic logging configuration for debugging purposes
# log_config = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "formatter": "default",
#         },
#     },
#     "loggers": {
#         "": {  # root logger
#             "level": "INFO",
#             "handlers": ["console"],
#         },
#         "myapp": {
#             "level": "DEBUG",
#             "handlers": ["console"],
#             "propagate": False,
#         },
#     },
# }

# logging.config.dictConfig(log_config)
# logger = logging.getLogger("myapp")
