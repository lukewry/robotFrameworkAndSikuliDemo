# -*- coding: utf-8 -*-
from __future__ import with_statement

# IMPORTANT: python level import - don´t mix it with java level imports of Sikuli classes
# like from org.sikuli.script import Region
# For more details go here: https://answers.launchpad.net/sikuli/+question/261129
#from sikuli import *
from sikuliwrapper import *

addImagePath("calc.sikuli")

s = Screen()

class Calculator(BaseLogger):
	ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
	def __init__(self):
		self.appCoordinates = (0, 0, 1024, 768)

	def clickSearch(self):
		    click("1522966761650.png")

        def goHome(self):
            if exists("1522967571129.png"):
                click("1522967588490.png")
                wait("1522967610674.png", 3)

        def clickMore(self):
            click("1522967974994.png")
#            wait("1523038062849.png",3)
            

        def searchVal(self, *args):
            click("1522968370460.png")
            wait("1523038633069.png", 3)
            
            zip = str(args[0])
            type(("%s" % args[0]) + Key.ENTER)

        def verify92123(self):
            wait("1523036453129.png",3)
            if exists("1522985172150.png"):
                self.log.passed("\nPASS: is 92123 zipcode")
            else:
                self.log.failed("\nFAIL: is not 92123 zipcode")

        def verifyInvalidZipInput(self):
            wait("1522985384737.png",3)
            if exists("1522985404024.png"):
                self.log.passed("\nPASS: verifies invalid input")
                click("1522985662677.png")
                
            else:
                self.log.failed("\nFAIL: accepts invalid input")
            
            
            
            
                
		
	def runTest(self):
		self.goHome()        
		self.clickSearch()
		self.goHome()		
		self.clickMore()
		self.searchVal(92123)
		self.verify92123()
		self.goHome()		
		self.clickMore()
		self.searchVal("94323jsdfn")
		self.verifyInvalidZipInput()		

if __name__ == "__main__":
	calc = Calculator()
	calc.runTest()
