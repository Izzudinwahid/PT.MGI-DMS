from random import random
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
from twisted.internet.task import LoopingCall
from threading import Thread
from time import sleep
import os
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temperature = 0


# class Temp(Thread):
#     """
#      A class for getting the current temp of a DS18B20
#     """

#     def __init__(self, fileName=''):
#         Thread.__init__(self)
#         self.tempDir = '/sys/bus/w1/devices/'
#         list = os.listdir(self.tempDir)
#         if(list[0][:2] == "28"):
#             fileName = list[0]
#         self.fileName = fileName
#         self.currentTemp = -999
#         self.correctionFactor = 1
#         self.enabled = True

#     def run(self):
#         while True:
#             if self.isEnabled():
#                 try:
#                     f = open(self.tempDir + self.fileName + "/w1_slave", 'r')
#                 except IOError as e:
#                     # print "Error: File " + self.tempDir + self.fileName + "/w1_slave" + " does$
#                     return

#                 lines = f.readlines()
#                 crcLine = lines[0]
#                 tempLine = lines[1]
#                 result_list = tempLine.split("=")

#                 temp = float(result_list[-1])/1000  # temp in Celcius
#                 temp = temp + self.correctionFactor  # correction factor
#                 # if you want to convert to Celcius, comment this line
#                 temp = (9.0/5.0)*temp + 32

#                 if crcLine.find("NO") > -1:
#                     temp = -999
#                 self.currentTemp = temp
#                 #print "Current: " + str(self.currentTemp) + " " + str(self.fileName)
#             sleep(1)

#     # returns the current temp for the probe
#     def getCurrentTemp(self):
#         return self.currentTemp

#     # setter to enable this probe
#     def setEnabled(self, enabled):
#         self.enabled = enabled
#     # getter

#     def isEnabled(self):
#         return self.enabled


def updating_writer(a):
    context = a[0]
    register = 3
    slave_id = 0x00
    address = 0x00
    #print pi.getCurrentTemp(),str(int(pi.getCurrentTemp()*10))
    values = [int(random(0, 1)*100)]
    context[slave_id].setValues(register, address, values)


store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),
    co=ModbusSequentialDataBlock(0, [0]*100),
    hr=ModbusSequentialDataBlock(0, [0]*100),
    ir=ModbusSequentialDataBlock(0, [0]*100))
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'
# pi = Temp()
# pi.start()
time = 5  # 5 seconds delaytime = 5 # 5 seconds delay
loop = LoopingCall(f=updating_writer, a=(context,))
loop.start(time, now=False)  # initially delay by time
StartTcpServer(context, identity=identity, address=("192.168.2.7", 2001))
# change localhost to your ip address.
