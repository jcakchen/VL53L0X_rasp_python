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
	def __init__(self,
				 sensor_object = VL53L0X.VL53L0X(),
				 scan_time = 0.05
				):
		"""scan the ranging sensor to detect anything close,
			then tell the master state
		Args:
			sensor_object: sensor type VL53L0X or VL6180X
			state: indicate anything close or nothing close or sensor error 
		"""
		self.range = threading.Thread(target=self.ranging)
		self.sensor_object = sensor_object
		self.scan_time = scan_time
		self.callback = None
	def __del__(self):
		self.sensor_object.stop_ranging()
		
	def start(self):
		""" start the threading to range  """
		self.range.start()
		
	def start_ranging(self):
		"""
		initialize the sensor and start ranging
		"""
		self.sensor_object.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
		
	def ranging(self, callback):
		"""get distance """
		self.start_ranging()
		while True:
			get_data = self.sensor_object.get_distance()
			if 0 <= get_data <= 600:
				print("CLOSE %d" % get_data)
				if callback:
					self.callback = callback
					self.callback()
			time.sleep(self.scan_time)	
			
			
			
