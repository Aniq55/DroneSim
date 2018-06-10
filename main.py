from uav import UAV
from survivor import survivor
import time
import threading

from constants import *
from chaos import random_pos, random_val

for i in range(nD):
    DRONES.append(UAV(i, random_pos(), random_pos(), Vmax, Vmax ))

for i in range(nS):
    SURVIVORS.append(survivor(i, random_pos(), random_pos()))

for i in range(nD) :
	process = threading.Thread(target=DRONES[i].search_survivors(), args=None )
	process.start()
	missions.append(process)
