#! /usr/bin/python3

import os, argparse, sys

def parseargs():
    cli_args = argparse.ArgumentParser(description="Change fan speed")
    cli_args.add_argument('--mode',help="no fan = 1, normal = 3, cooler booster = 4 ", default='3', type=int)
    options = cli_args.parse_args(sys.argv[1:])
    return options


def write_EC(v, battery_threshold):
	with open(EC_IO_FILE, 'r+b') as file:
		if v[0] == 128:
			file.seek(0x98)
			file.write(bytes((128,)))
			file.seek(0xf4)
			file.write(bytes((0,)))
		else:
			file.seek(0x98)
			file.write(bytes((0,)))
			file.seek(0xf4)
			file.write(bytes((v[0],)))
			file.seek(114)
			file.write(bytes((v[1],)))
			file.seek(115)
			file.write(bytes((v[2],)))
			file.seek(116)
			file.write(bytes((v[3],)))
			file.seek(117)
			file.write(bytes((v[4],)))
			file.seek(118)
			file.write(bytes((v[5],)))
			file.seek(119)
			file.write(bytes((v[6],)))
			file.seek(120)
			file.write(bytes((v[7],)))
			file.seek(138)
			file.write(bytes((v[8],)))
			file.seek(139)
			file.write(bytes((v[9],)))
			file.seek(140)
			file.write(bytes((v[10],)))
			file.seek(141)
			file.write(bytes((v[11],)))
			file.seek(142)
			file.write(bytes((v[12],)))
			file.seek(143)
			file.write(bytes((v[13],)))
			file.seek(144)
			file.write(bytes((v[14],)))
		"""file.seek(239)
		file.write(bytes((battery_threshold)))"""
	return


EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'
battery_threshold = 100

options = parseargs()
mode = options.mode
if (mode != 1 ) and ( mode != 3) and ( mode != 4):
	print("wrong mode")
	exit()


if int(mode) == 1:
	vr = [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	print(vr)
	write_EC(vr, battery_threshold)
elif int(mode) == 3:
	vr = [140, 0, 20, 40, 55, 70, 85, 100, 0, 20, 40, 55, 70, 85, 100]
	print(vr)
	write_EC(vr, battery_threshold)
elif int(mode) == 4:
	with open(EC_IO_FILE,'w+b') as file:
		file.seek(0x98)
		file.write(bytes((128,)))
		file.seek(0xef)
		file.write(bytes((battery_threshold,)))


