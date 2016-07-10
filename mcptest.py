#!/usr/bin/env python

import time
import sys
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0))

while True:
    for i in range(0,8):
        if i == 0:
            sys.stdout.write('{0}'.format(mcp.read_adc(i)))
        else:
            sys.stdout.write(',{0}'.format(mcp.read_adc(i)))
    print('')
    time.sleep(1.0)

