from pyfirmata import Arduino, util
import time
board = Arduino("COM3")
i=0
i=int(input())
j=0
while j<=i:
    board.digital[9].write(0)
    time.sleep(0.2)
    board.digital[9].write(1)
    time.sleep(0.2)
    j=j+1
board.digital[9].write(0)
