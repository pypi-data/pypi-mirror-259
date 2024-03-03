# DFRobot_GP8403
#### Fork from [DFRobot GP8403](https://github.com/DFRobot/DFRobot_GP8403/) to bring this module to pypi.

This I2C to 0-5V/0-10V DAC module can be used to output voltage of 0-5V or 0-10V. It has the following features:
1. Output voltage of 0-5V or 0-10V.
2. It can control the output voltage with an I2C interface, the I2C address is default to be 0x58. 
3. The output voltage config will be lost after the module is powered down. Save the config if you want to use it for the next power-up.

## Table of Contents
  - [Summary](#summary)
  - [Installation](#installation)

## Summary
The Arduino library is provided for the I2C 0-5V/0-10V DAC module to set and save the output voltage config of the module. And the library has the following functions:
1. Set the voltage of 0-5V or 0-10V directly；
2. Output the corresponding voltage by setting the DAC range of 0-0xFFF；
3. Save the voltage config(Will not be lost when powered down).

## Installation
Install Module with pip<br>
```python
pip install DFRobot-GP8403
```

## Example
```python
import time
from DFRobot.DAC import GP8403

DAC = GP8403(0x58)
while DAC.begin() != 0:
    print("init error")
    time.sleep(1)
print("init succeed")

#Set output range
DAC.set_DAC_outrange(DAC.OUTPUT_RANGE_10V)

#Output value from DAC channel 0
DAC.set_DAC_out_voltage(4200,DAC.CHANNEL0)
```
Find more examples in `examples` folder
