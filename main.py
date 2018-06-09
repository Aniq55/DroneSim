from uav import UAV
from survivor import survivor
import time
import threading

from constants import *
from chaos import random_pos, random_val

for i in range(nD):
    DRONES.append(UAV(i, random_pos(), random_pos(), Vmax*random_val(), Vmax*random_val() ))

for i in range(nS):
    SURVIVORS.append(survivor(i, random_pos(), random_pos()))

# RUN parallel threads for the drones and monitor the len(SURVIVORS) value
def monitor():
    while len(SURVIVORS)>0 :
        time.sleep(1)
        print(len(SURVIVORS))

for i in range(nD) :
	process = threading.Thread(target=DRONES[i].search_survivors(), args=None )
	process.start()
	missions.append(process)
