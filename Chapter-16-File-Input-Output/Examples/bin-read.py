file = open("Chips", "rb")

byte = file.read(1)
while byte:
    print(byte)
    byte = file.read(1)