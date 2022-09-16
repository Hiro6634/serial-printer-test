import serial

ASCII_TAB = '\t' 
ASCII_LF =  '\n' 
ASCII_FF =  '\f' 
ASCII_CR =  '\r' 
ASCII_EOT =   4  
ASCII_DLE =  16  
ASCII_DC2 =  18  
ASCII_ESC =  27  
ASCII_FS =   28  
ASCII_GS =   29

string = "HoLa MuNdO"

with serial.Serial('COM4',38400, timeout=1) as ser:
    packet = bytearray()
    packet.append(ASCII_ESC)
    packet.append(bytes('@', 'ascii')[0])
    packet.append(ASCII_GS)
    packet.append(bytes('!','ascii')[0])
    for byte in bytes(string,'ascii'):
        packet.append(byte)
    packet.append(ASCII_ESC)
    packet.append(bytes('d','ascii')[0])
    packet.append(5)
    packet.append(ASCII_ESC)
    packet.append(bytes('m','ascii')[0])
    
    for byte in packet:
        str = "0x{0:02X} {1:03d} {2:c}".format(byte,byte,byte)
        print(str)
    ser.write(packet)