
#Author Michael
#Date 12/08/23
#attempt to fix activated servos
import time

try:
    from adafruit_register.i2c_struct import UnaryStruct
    from adafruit_register.i2c_struct_array import StructArray
    from adafruit_bus_device import i2c_device

    from typing import Optional, Type
    from types import TracebackType
    from busio import I2C
except ImportError:
    pass

def __enter__(self) -> "PCA9685":
        return self

def __exit__(
    self,
    exception_type: Optional[Type[type]],
    exception_value: Optional[BaseException],
    traceback: Optional[TracebackType],
) -> None:
    self.deinit()

def deinit(self) -> None:
    """Stop using the pca9685."""
    self.reset()

deinit()