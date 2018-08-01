#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2018 Jack Chen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import threading
import time
import VL53L0X



class Range(object):
	""" Detect anything close to the sensor"""
	CLING = 0
	CLOSE = 1
	FAR = 2
	def __init__(self,
				 sensor_object,
				 distance = 0,
				 scan_time = 0.1
				):
		"""scan the ranging sensor to detect anything close,
			then tell the master status
		Args:
			sensor_object: sensor type VL53L0X or VL6180X
			distance: distance from object to sensor
			status: indicate anything close or nothing close or sensor error 
		"""
		self.range = threading.Thread(target=self._ranging)
		self.sensor_object = VL53L0X.VL53L0X()
		self.distance = distance
		self.scan_time = scan_time
		
		self.status = None
	def __del__(self):
		self.sensor_object.stop_ranging()
	def start(self)
		""" start the threading to range  """
		self.start_ranging()
		self.range.start()
	def start_ranging(self):
		"""
		initialize the sensor and start ranging
		"""
		self.sensor_object.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
	def _ranging(self):
		"""get distance """
		while True:
			self.distance = self.sensor_object.get_distance()
			if self.distance < 60
				self.status = CLING
				print("CLING%d" % self.distance)
			elif 60 <= self.distance <= 200
				self.status = CLOSE
				print("CLOSE%d" % self.distance)
			else self.distance >200
				self.status = FAR
				print("FAR%d" % self.distance)
			time.sleep(self.scan_time)

def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)
    Range().start()			
if __name__ == '__main__':
    main()			
			
			
