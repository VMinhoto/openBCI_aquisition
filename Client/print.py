from __future__ import print_function
import sys

sys.path.append('..')  # help python find cyton.py relative to scripts folder
from openbci import cyton as bci
import logging
import time


def printData(sample):
    # os.system('clear')
    print("----------------")
    print("%f" % (sample.id))
    print(sample.channel_data)
    print(sample.aux_data)
    print("----------------")


if __name__ == '__main__':
    # port = '/dev/tty.OpenBCI-DN008VTF'
    port = 'COM3'
    # port = '/dev/tty.OpenBCI-DN0096XA'
    baud = 115200
    logging.basicConfig(filename="test.log", format='%(asctime)s - %(levelname)s : %(message)s', level=logging.DEBUG)
    logging.info('---------LOG START-------------')
    board = bci.OpenBCICyton(port=port, scaled_output=False, log=True)
    print("Board Instantiated")
    board.ser.write(str.encode('v'))
    time.sleep(10)
    board.start_streaming(printData)
    board.print_bytes_in()