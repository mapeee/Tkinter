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

import h5py

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
    return name

def gruppen_HDF5(Datenbank):
    Datenbank = Datenbank.get()
    file5 = h5py.File(Datenbank,'r+') ##HDF5-File
    gruppen = file5.keys()
    print gruppen
    return gruppen


##hdf = "V:\\Forschungsprojekte\\laufende Projekte\\MRH-Erreichbarkeit\\09Berechnungen\\01Datenbanken\\MRH_alt.h5"
