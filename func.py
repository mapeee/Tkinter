#-------------------------------------------------------------------------------
# Name:        Functions for Accessibility-tools
# Purpose:
#
# Author:      mape
#
# Created:     12/12/2017
# Copyright:   (c) mape 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from tkFileDialog import askopenfilename

#--Functions--#
def rechnen ():
    print "test"
    print "Modul:" +__name__

def ausgeben ():
    print "rechnen"

def callback(v):
    name = askopenfilename()
    v.set(name)