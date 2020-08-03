'''ecoding.py provides utilities for compressing a file of data
using a 'delta' encoding (change over the previous) element.
'''
import struct
import os.path
from os import path
#TODO 1. Write a function that loads the input data 
#and returns a list of numbers
def load_orig_file(in_filename):
	if not path.exists(in_filename):
		raise Exception('File does not exist')
	data_file = open(in_filename, "r")
	number_strings = data_file.read().splitlines()
	numbers = [int(i) for i in number_strings]
	return numbers
	'''load_orig_file takes an input file and returns a list of
	   numbers. The file is formatted with a single integer
	   number on each line
	'''

#TODO 2. Write a function that performs the delta encoding
def delta_encoding(data):
	new_list = [data[0]]
	for x in range(1, len(data)):
		new_list.append(data[x]-data[x-1])
	return new_list
	'''delta_encoding takes a list of integers and performs
	   a delta encoding represent each element as a difference
	   from the previous one. The first element is kept as is.

	   delta_encoding encoding returns a list where the first
	   element is the original value and all the rest of the
	   elements are deltas from the first value.
	'''

#TODO 3. Apply a shift to all the elements so all the deltas are positive
def shift(data, offset):
	data = [i+offset for i in data]
	return data
	'''shift adds 'offset' to all of the elements to ensure that
	   every value in the delta encoding is positive.
	'''

#GIVEN, should be obvious what it does
def unshift(data, offset):
	return shift(data,-offset)

#TODO 4. Convert the encoded data into a byte array and write
#to disk.
def write_encoding(data, out_file):
	f = open(out_file, "wb")
	binary_data = bytearray(data)
	f.write(binary_data)
	f.close()
	return 0


#GIVEN, read encoded file
def read_encoding(out_file):
	f = open(out_file, 'rb')
	encoded = f.read()
	return struct.unpack("B"*len(encoded), encoded)


#TODO 5. Write a function that performs the delta encoding
def delta_decoding(data):
	decoded_data = [data[0]]
	for x in range(1, len(data)):
		decoded_data.append(data[x]+sum(data[0:x]))  
	return decoded_data
	'''delta_decoding takes a delta encoded list and return 
	   the original data.
	'''
