# -*- coding: utf-8 -*-
from __future__ import with_statement

# IMPORTANT: python level import - don´t mix it with java level imports of Sikuli classes
# like from org.sikuli.script import Region
# For more details go here: https://answers.launchpad.net/sikuli/+question/261129
#from sikuli import *
import sys
sys.path.append('C:<location>\calc.sikuli')
from sikuliwrapper import *

addImagePath("testRedFin.sikuli")

s = Screen()

class TestRedFin(BaseLogger):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    def __init__(self):
        
        self.appCoordinates = (0, 0, 1024, 768)

    def openRedFinTab(self):
        click("1523315889113.png")
        wait("1523315917138.png")
        type("https://www.redfin.com" + Key.ENTER)
        wait("1523316009118.png",3)
        if exists("1523316031852.png"):
            self.log.passed("\nPASS: Opened Red Fin")
        else:
            self.log.failed("\nFAIL: Didn't open Red Fin")
                
        
        
    def runTest(self):
        self.openRedFinTab()

if __name__ == "__main__":
	test = TestRedFin()
	test.runTest()
