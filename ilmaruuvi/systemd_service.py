#!python
# -*- coding: utf-8 -*-
from os import path

def install():
    filename = 'ilmaruuvi.service'
    install_path = path.join('/etc/systemd/system', filename)
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, filename), encoding='utf-8') as f:
        service = f.read()
    service = service.format(working_dir=here, exec_start='python ' + here)
    with open(install_path, 'w') as f:
        f.write(service)