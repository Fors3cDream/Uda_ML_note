"""
Create by Killer at 2019-05-16 16:00
"""

import itertools
import sys
import time

symbols = itertools.cycle('-\|/')

while True:
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush()
    time.sleep(0.1)