from pyfirmata import Arduino, util
import time

board = Arduino("/dev/cu.usbserial-AL008BFQ")
it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()

print("Iniciando...")
while True:
    print(board.analog[0].read())
    board.pass_time(1)
    if board.analog[0].read() < 0.5:
        board.digital[6].write(1)
    else:
        board.digital[6].write(0)
print("Finalizando...")
board.exit()
