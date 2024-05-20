from controller import Robot
from controller import Motor
from controller import Altimeter
from controller import LED
import math

self.front_led=self.getDevice("front_led")
self.left_led=self.getDevice("left_led")
self.right_led=self.getDevice("right_led")
self.back_led=self.getDevice("back_led")
self.left_motor = self.getDevice("left wheel motor")
self.right_motor = self.getDevice("right wheel motor")
self.left_motor.setPosition(math.inf)
self.right_motor.setPosition(math.inf)
self.left_motor.setVelocity(2.0)
self.right_motor.setVelocity(2.0)
self.direction_switch = False
self.acc=[]



class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timeStep = 32  # set the control time step

        # get device tags
        # self.distanceSensor = self.getDistanceSensor('my_distance_sensor')
        # self.led = self.getLed('my_led')
        # self.distanceSensor.enable(timeStep)  # enable sensors to read data from them
        
        self.altimeter=self.getDevice("altimeter")
        self.altimeter.enable(self.timeStep)
        
        
        self.direction_switch = False


    def run(self):
            
        while self.step(self.timeStep) != -1:
        
            # get the time step of the current world.
            
            altitude = self.altimeter.getValue()
            print(self.accelerometer.getValues())
            for i in range(0,3):
                self.accValues.append(self.accelerometer.getValues())
            # print(altitude)
            if (abs(self.accValues[1] >abs(self.accValues[0]):
                self.front_led.set(false)
                self.back_led.set(false)
                self.right_led.set(self.accValues[1]>0)
                self.left_led.set(self.accValues[1]<0)
                
            else:
                self.front_led.set(self.accValues[1]>0)
                self.back_led.set(self.accValues[1]<0)
                self.right_led.set(false)
                self.left_led.set(false)
            
                
                
# main Python program
controller = MyController()
controller.run()
