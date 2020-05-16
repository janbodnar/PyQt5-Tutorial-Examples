#!/usr/bin/python

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print('Gregorian date for today:', now.toString(Qt.ISODate))
print('Julian day for today:', now.toJulianDay()) 
