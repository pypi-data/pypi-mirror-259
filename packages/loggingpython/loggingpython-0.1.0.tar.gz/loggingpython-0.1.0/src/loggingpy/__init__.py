from .logger import Logger


__all__ = ["Logger"]


def hello_from_logpy() -> None:
    print("Hello from the loggingpy community. \
https://github.com/mr-major-k-programmer/logpy")


def getLogger() -> Logger:
    return Logger()


if __name__ == '__main__':
    pass
else:
    hello_from_logpy()
