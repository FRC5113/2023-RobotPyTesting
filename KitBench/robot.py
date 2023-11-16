#!/usr/bin/env python3
"""
    Kitbot chassis, sample program.
"""

import wpilib
from wpilib.drive import DifferentialDrive
from ctre import WPI_TalonSRX


def curve(raw):
    return (raw ** 3) * 0.3

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""

        # object that handles basic drive operations
        self.frontLeftMotor = WPI_TalonSRX(2)
        self.rearLeftMotor = WPI_TalonSRX(3)
        self.frontRightMotor = WPI_TalonSRX(4)
        self.rearRightMotor = WPI_TalonSRX(5)

        self.left = wpilib.MotorControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.MotorControllerGroup(
            self.frontRightMotor, self.rearRightMotor
        )
        self.right.setInverted(True)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.myRobot.arcadeDrive(curve(self.leftStick.getY()), -curve(self.leftStick.getX()))


if __name__ == "__main__":
    wpilib.run(MyRobot)
