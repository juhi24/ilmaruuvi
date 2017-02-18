# -*- coding: utf-8 -*-
import time
from datetime import datetime
from ruuvitag_sensor.ruuvi import RuuviTagSensor

def main():
    logfile = '/var/log/ilmaruuvi.log'
    MAC1 = 'E8:A8:F2:B1:AE:A3'
    sensor = RuuviTagSensor(MAC1)
    while True:
        state = sensor.update()
        now = datetime.today()
        database_file = '/var/lib/ilmaruuvi/{}.csv'.format(now.strftime('%Y%m%d'))
        with open(database_file, 'a') as f:
            f.write('{time},{t},{rh},{p}\n'.format(time=now.strftime('%Y-%m-%d %H:%M:%S'),
						 t=state['temperature'],
					   	 rh=state['humidity'],
					    	 p=state['pressure']))
        time.sleep(880)

if __name__ == "__main__":
    # execute only if run as a script
    main()
