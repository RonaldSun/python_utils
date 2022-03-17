import signal


class GracefulExit(Exception):
    pass


def signal_handler(signum, frame):
    raise GracefulExit()


def EnableGracefulExit():
    signal.signal(signal.SIGINT, signal_handler)
