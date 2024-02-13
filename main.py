import time
from encoder import Encoder
from decoder import Decoder
from utils import *
import os
import filecmp


# Generate the binary file (input for encoder)
if not os.path.exists('originFileNameBin'):
    with open(originFileName, 'rb') as file:
        with open(originFileNameBin, 'w') as fileBin:
            text = file.read().decode('utf-8')
            binaryText = ''.join(format(ord(char), '08b') for char in text)
            fileBin.write(binaryText)

# Encode and decode the file
startTime = time.time()
#encoder = Encoder(originFileNameBin)
#encoder.encode(defMultiplicity, encodedFileName)
print("Time to encode: ", time.time() - startTime)

# Decode the file
startTime = time.time()
decoder = Decoder(encodedFileName)
decoder.decode(decodedFileNameBin)
print("Time to decode: ", time.time() - startTime)

startTime = time.time()
with open(decodedFileNameBin, 'rb') as fileBin:
    with open(decodedFileName, 'w') as file:
        binaryText = fileBin.read().strip().decode('utf-8')
        file.write(''.join(chr(int(binaryText[i:i+8], 2)) for i in range(0, len(binaryText), 8)))


bin_files_equal = filecmp.cmp(originFileNameBin, decodedFileNameBin)
if bin_files_equal:
    print("The binary files are identical.")
else:
    print("The binary files are different.")

are_files_equal = filecmp.cmp(originFileName, decodedFileName)

if are_files_equal:
    print("The files are identical.")
else:
    print("The files are different.")

print("Time to convert binary to text: ", time.time() - startTime)
