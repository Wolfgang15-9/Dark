import math

class PCA9685:
    # ... existing methods ...

    def set_servo_pulse(self, channel: int, pulse: int) -> None:
        """Sets the Servo Pulse, Correct for the offset."""
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 50       # 60 Hz
        pulse_length //= 4096     # 12 bits of resolution
        pulse *= 1000
        pulse //= pulse_length
        self.set_pwm(channel, 0, pulse)

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
        pulse = angle * (2000 / 180) + 500

        # Set the PWM signal for each servo on the given arm
        for channel in arms[arm]:
            self.set_servo_pulse(channel, pulse)

# Use the PCA9685 class
with PCA9685() as pca:
    # Test the servos on arm 1 with a rotation of 90 degrees
    pca.test_servos(1, 90)