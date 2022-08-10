from pymodbus.client.sync import ModbusSerialClient as ModbusClient

buff_client = ModbusClient(method='rtu', port='/dev/ttyUSB0',
                           stopbits=1, bytesize=8, parity='N', baudrate=19200, timeout=.500)


baca = buff_client.read_holding_registers(address = 20,count =1,unit= 1)

print(baca.registers)
