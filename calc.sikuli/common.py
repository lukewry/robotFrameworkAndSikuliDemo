# -*- coding: utf-8 -*-

# Global variables, can be moved to config file
cfgImageLibrary = "C:<location>\calc.sikuli" # image search directory
cfgLoggingLevel = "debug" # logging level, possible values 'debug', 'info'

# Custom Exception for verification failures
class VerificationFailed(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return self.value
