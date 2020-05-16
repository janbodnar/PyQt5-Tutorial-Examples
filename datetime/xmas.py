#!/usr/bin/python

from PyQt5.QtCore import QDate

xmas1 = QDate(2019, 12, 24)
xmas2 = QDate(2020, 12, 24)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print(f'{dayspassed} days have passed since last XMas')

nofdays = now.daysTo(xmas2)
print(f'There are {nofdays} days until next XMas')
