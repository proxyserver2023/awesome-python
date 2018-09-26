#!/usr/bin/env python

class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("Driving")

    def __updateSoftware(self):
        print("Updating Software")

redcar = Car()
redcar.drive()
redcar.__updateSoftware()

# The private methods and attributes are not actually hidden, they're renamed adding "_Car" in the beginning of their name.
#
# The method can actually be called using redcar._Car__updateSoftware()

redcar._Car__updateSoftware()
