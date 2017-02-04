#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jussi Tiira
"""
import time
from ruuvitag_sensor.ruuvi import RuuviTagSensor

MAC1 = 'E8:A8:F2:B1:AE:A3'
sensor = RuuviTagSensor(MAC1)
while True:
    state = sensor.update()
    print(state)
    time.sleep(10)
