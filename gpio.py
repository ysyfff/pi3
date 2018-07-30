import RPi.GPIO as io


def init(fn):
    def wrapper():
        io.setmode(io.BOARD)
        fn()
    return wrapper


def init2(port, in_or_out):
    def decorator(fn):
        def wrapper(*args, **kw):
            io.setmode(io.BOARD)
            io.setup(port, in_or_out)
            fn(*args, **kw)
        return wrapper
    return decorator


if __name__ == '__main__':
    init()
