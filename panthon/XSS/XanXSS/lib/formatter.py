import time


def debug(string):
    """Output a dark blue debug string."""
    timer = time.strftime("%H:%M:%S")
    print("\033[36m[debug]\033[0m[{}] {}".format(timer, string))


def info(string):
    """Output a light green information string."""
    timer = time.strftime("%H:%M:%S")
    print("\033[1m\033[92m[info][{}]\033[0m {}".format(timer, string))


def warning(string):
    """Output a dark yellow warning string."""
    timer = time.strftime("%H:%M:%S")
    print("\033[33m[warning][{}]\033[0m {}".format(timer, string))


def error(string):
    """Output a red error string."""
    timer = time.strftime("%H:%M:%S")
    print("\033[91m[error][{}]\033[0m {}".format(timer, string))
