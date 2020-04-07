#-------------------------------------------------------------------------------
# Name:        VISUM-functions
# Purpose:
#
# Author:      mape
#
# Created:     21/12/2017
# Copyright:   (c) mape 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import win32com.client.dynamic


def main():
    pass

if __name__ == '__main__':
    main()

path = ""

def open(path):
    path = path.get()
    VISUM = win32com.client.dynamic.Dispatch("Visum.Visum.15")
    VISUM.loadversion(path)
    a = len(VISUM.net.Stops.GetAll)

    print "--Stops: "+str(a)+"--"
    print "--erfolgreich durchgefuehrt--"