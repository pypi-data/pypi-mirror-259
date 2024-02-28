'''
Check your EEPROM address using: sudo i2cdetect -y 1

  AT24C32 Code
  datasheet: atmel.com/Images/doc0336.pdf
'''
import smbus
from time import sleep

class AT24Cxxx:
    def __init__(self, channel:int = 1, address:int = 0x50) -> None:
        self.address = address
        self.bus = smbus.SMBus(channel)

    def setAddress(self, EEPROM_Memory_Address) -> None:
        a1 = int(EEPROM_Memory_Address/256)
        a0 = int(EEPROM_Memory_Address % 256)

        self.bus.write_i2c_block_data(self.address, a1, [a0])

    def readByte(self, EEPROM_Memory_Address) -> int:

        self.setAddress(EEPROM_Memory_Address)
        return self.bus.read_byte(self.address)
    
    def readChar(self, EEPROM_Memory_Address) -> str:

        self.setAddress(EEPROM_Memory_Address)
        return bytes([self.bus.read_byte(self.address)]).decode()
    
    def readString(self, EEPROM_Memory_Address) -> str:
        byteRead = self.readChar(EEPROM_Memory_Address)
        str = ''
        while byteRead != '\0':
            str = str + byteRead
            EEPROM_Memory_Address = EEPROM_Memory_Address + 1
            byteRead = self.readChar(EEPROM_Memory_Address)
        return str

    def writeByte(self, EEPROM_Address, value) -> None:
        a1 = int(EEPROM_Address/256)
        a0 = int(EEPROM_Address % 256)

        self.bus.write_i2c_block_data(self.address, a1, [a0, value])
        sleep(0.01)

    def writeString(self, EEPROM_Address, value:str) -> None:
        byteArray = value.encode()
        add = EEPROM_Address
        for byteVal in byteArray:
            self.writeByte(add, byteVal)
            add = add + 1
