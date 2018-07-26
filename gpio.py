import RPi.GPIO as io

def init(fn):
    def wrapper():
        io.setmode(io.BOARD)
        fn()
    return wrapper


if __name__ == '__main__':
    init()
