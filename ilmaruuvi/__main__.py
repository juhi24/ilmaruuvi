# -*- coding: utf-8 -*-
import time
from ruuvitag_sensor.ruuvi import RuuviTagSensor

def main():
    database_file = '/var/lib/ilmaruuvi/db.hdf'
    logfile = '/var/log/ilmaruuvi.log'
    MAC1 = 'E8:A8:F2:B1:AE:A3'
    sensor = RuuviTagSensor(MAC1)
    while True:
        state = sensor.update()
        with open(logfile, 'a') as f:
            f.write(str(state + '\n'))
        time.sleep(10)

if __name__ == "__main__":
    # execute only if run as a script
    main()