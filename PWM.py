#!/usr/bin/python3

from board import SCL, SDA
import busio
import sys
from adafruit_pca9685 import PCA9685

def main(argv):
    #print(sys.argv[1])
    i2c_bus = busio.I2C(SCL,SDA)
    pca = PCA9685(i2c_bus)
    pca.frequency = int(sys.argv[1])
    mult1 = float(sys.argv[2])
    mult2 = float(sys.argv[3])
    pca.channels[0].duty_cycle = round(65535*mult1)
    pca.channels[1].duty_cycle = round(65535*mult2)

if __name__ == "__main__":
    main(sys.argv[1:])
