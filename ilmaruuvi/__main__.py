# -*- coding: utf-8 -*-
import time
from ruuvitag_sensor.ruuvi import RuuviTagSensor

def main():
    MAC1 = 'E8:A8:F2:B1:AE:A3'
    sensor = RuuviTagSensor(MAC1)
    while True:
        state = sensor.update()
        print(state)
        time.sleep(10)

if __name__ == "__main__":
    # execute only if run as a script
    main()