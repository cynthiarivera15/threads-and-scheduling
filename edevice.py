# Cynthia Marie Rivera Sánchez
# 801-19-5470
# CCOM4017 - 002
# Projetc 1

from threading import Thread
from time import sleep
import socket
import random

MAX_CPU_RANGE = 10
devices = 2

#Class to implement a python Thread.  Inheit all the functions from Thread

class Edevice(Thread):

    # The constructor assign the internal id to the new thread.
    def __init__ (self, t_number):

        # This variable is used to assign an internal id to the thread.
        self.t_number = t_number
        Thread.__init__(self)

    # Define inside what the thread is to do.
    def run(self):
        serverAddressPort = ("127.0.0.1", 20001)

        bufferSize = 1024

        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

        while(True):
            msgFromClient = "%s:%s" %(self.t_number, random.randint(1, MAX_CPU_RANGE - 1))

            bytesToSend = str.encode(msgFromClient)

            # Send to server using created UDP socket
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            sleep(random.randint(1,5))

        # msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        # msg = "Message from Server {}".format(msgFromServer[0])

        print("Thread %s finished" % self.t_number)


# Python main funtion.  Not necessary but to keep your C++ legacy...
def main():

    # In kernel threads you would like to set this variable
    # to the number of cores in the system.

    thread = [0] * devices # [0, 0]

    # Create and start the threads
    for i in range(devices):
        thread[i] = Edevice(i)
        thread[i].start()

    # Make the original thread wait for the created threads.
    for i in range(devices):
        thread[i].join()

if __name__ == "__main__":
    main()
