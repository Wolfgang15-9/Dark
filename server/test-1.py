
import math
from Adafruit_PCA9685 import PCA9685

# Install the required package
# pip install adafruit-circuitpython-pca9685 

class MyClass:
    def __init__(self):
        self.pca = PCA9685()

    def set_servo_pulse(self, channel, pulse):
        pulse_length = 4096  # 12 bits of resolution
        pulse *= 1000
        pulse //= pulse_length
        self.pca.set_pwm(channel, 0, pulse)

    def test_servos(self, arm: int, angle: int) -> None:
        """Test the servos on a given arm."""

        # Define which PWM channels correspond to each arm
        arms = {
            1: [0, 1, 2],  # PWM channels for arm 1
            2: [3, 4, 5],  # PWM channels for arm 2
            3: [6, 7, 8],  # PWM channels for arm 3
            4: [9, 10, 11]  # PWM channels for arm 4
        }

        # Calculate the pulse width for the given angle
        pulse = math.radians(angle) * (2000 / math.pi) + 500

        # Set the PWM signal for each servo on the given arm
        for channel in arms[arm]:
            self.set_servo_pulse(channel, pulse)

# Use the MyClass
my_obj = MyClass()
my_obj.test_servos(1, 90)
