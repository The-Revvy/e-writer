in_file = open("input.ek3", "rb")
out_file = open("inject.bin", "wb")

# .ek3 injection, probably a more efficient way to do this but I only started learning python today so give me a break
out_file.write(b"\x01\x00\x00\x00\x02\x02\x00\x02\x00\x00\x00\x04\x00\x80\x01\x00\x00\x10\x3D\xA5\x00\x00\x1E\x00\x00\x02\x95\x02\x00\x02\x05\x24\x00\x00\x02\x02\xB8\x61\x00\x00\x02\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x60\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x61\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x62\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x63\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x64\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x65\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x66\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x67\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x68\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x69\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x6a\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x6b\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x6c\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x6d\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x6e\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x6f\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x70\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x71\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x72\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x73\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x74\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x75\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x76\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x77\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x78\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x79\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x7a\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x7b\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x7c\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x7d\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x7e\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x7f\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x80\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x81\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x82\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x83\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x84\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x85\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x86\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x87\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x88\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x89\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x8a\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x8b\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x8c\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x8d\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x8e\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x8f\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x90\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x91\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x92\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x93\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x94\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x95\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x96\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x97\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x98\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x99\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x9a\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x9b\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x9c\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x9d\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x9e\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x9f\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa0\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa1\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa2\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa3\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa4\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa5\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa6\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa7\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa8\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xa9\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xaa\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xab\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xac\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xad\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xae\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xaf\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb0\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb1\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb2\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb3\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb4\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb5\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb6\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb7\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb8\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xb9\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xba\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xbb\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xbc\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xbd\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xbe\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xbf\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xc0\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xc1\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xc2\x43\x00\x03\x11")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\xc3\x43\x00\x03")
data = in_file.read(1)
out_file.write(data)
out_file.write(b"\x0D\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
in_file.close()
out_file.close()

# Checksum calculation, by Hatschky (https://github.com/hatschky/pokecarde/blob/master/scripts/checksum.py)

import struct
import sys

chunk_lengths = [0,0,0,6,2,5,12,5,3,1,2,5,5,5,1,13,13]

bytewises = []
bytewise_results = []
wordwises = []
wordwise_results = []
crcs = []
crc_results = []

data = ""
with open("inject.bin", 'rb') as f:
	data = f.read()
f.closed

base_address = struct.unpack('<I', data[1:5])[0]
i = 0x11 # first chunk location
while i < len(data):
	chunk_type = ord(data[i])
	if chunk_type == 0x02: # END_OF_CHUNKS
		break
	elif chunk_type == 0x07: # CUSTOM_BERRY
		start_address = struct.unpack('<I', data[i+1:i+5])[0] - base_address
		bytewises.append([start_address + 0x52C, start_address, start_address + 0x52C])
	elif chunk_type == 0x0D: # BATTLE_TRAINER
		start_address = struct.unpack('<I', data[i+1:i+5])[0] - base_address
		wordwises.append([start_address + 0xB8, start_address, start_address + 0xB8])
	elif chunk_type == 0x0F: # CHECKSUM_BYTES
		start_address = struct.unpack('<I', data[i+5:i+9])[0] - base_address
		end_address = struct.unpack('<I', data[i+9:i+13])[0] - base_address
		bytewise.append([i + 1, start_address, end_address])
	elif chunk_type == 0x10: # CHECKSUM_CRC
		start_address = struct.unpack('<I', data[i+5:i+9])[0] - base_address
		end_address = struct.unpack('<I', data[i+9:i+13])[0] - base_address
		crcs.append([i + 1, start_address, end_address])
	elif chunk_type < 0x02 or chunk_type > 0x10:
		print "Unknown chunk {0:X}".format(chunk_type)
		raise TypeError
	i += chunk_lengths[chunk_type]


# calculate and insert all wordwise checksums
for wordwise in wordwises:
	sum = 0
	for i in range(wordwise[1], wordwise[2], 4):
		sum = (sum + struct.unpack('<I', data[i:i+4])[0]) & 0xFFFFFFFF
	wordwise_results.append(sum)
i = 0
for wordwise in wordwises:
	data = data[0:wordwise[0]] + struct.pack('<I', wordwise_results[i]) + data[(wordwise[0] + 4):]
	i += 1


# calculate and insert all bytewise checksums
for bytewise in bytewises:
	sum = 0
	for i in range(bytewise[1], bytewise[2]):
		sum = (sum + ord(data[i])) & 0xFFFFFFFF
	bytewise_results.append(sum)
i = 0
for bytewise in bytewises:
	data = data[0:bytewise[0]] + struct.pack('<I', bytewise_results[i]) + data[(bytewise[0] + 4):]
	i += 1


# calculate and insert all CRC checksums
for crc in crcs:
	sum = 0x1121
	for i in range(crc[1], crc[2]):
		sum ^= ord(data[i])
		for j in range(8):
			if(sum & 1):
				sum = (sum >> 1) ^ 0x8408
			else:
				sum >>= 1
	sum = ~sum & 0xFFFF
	crc_results.append(sum)

i = 0
for crc in crcs:
	data = data[0:crc[0]] + struct.pack('<I', crc_results[i]) + data[(crc[0] + 4):]
	i += 1


# write the updated file
out = open("fixject.bin", 'wb')
out.write(data)
out.close()

# inject script into dotcode


dot_file = open("dotcode.z80", "rb")
out_file = open("card.z80", "wb")
in_file = open("fixject.bin", "rb")
data = dot_file.read(5450)
out_file.write(data)



data = in_file.read()
out_file.write(data)

dot_file.seek(6112)
data = dot_file.read()
out_file.write(data)
in_file.close()
out_file.close()
dot_file.close()

import os
os.remove("fixject.bin")
os.remove("inject.bin")
