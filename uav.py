from constants import *
import time
import threading
from chaos import *

class UAV():
    ID= None
    x= None
    y= None
    velx = None
    vely= None
    rescued = None

    def __init__(self, ID, x, y, velx, vely):
        self.ID= ID
        self.x= x
        self.y= y
        self.velx= velx
        self.vely= vely
        self.rescued = []
        self._time_ = time.time()
        self.init_time = self._time_

    def update_position(self, time_elapsed):
        self.x= ( self.x + self.velx*time_elapsed*random_val() )%L
        self.y= ( self.y + self.vely*time_elapsed*random_val() )%L

    def search_survivors(self):
        self.init_time = time.time()
        while len(SURVIVORS)>0:
            x_lower, x_upper = self.x - RANGE, self.x + RANGE
            y_lower, y_upper = self.y - RANGE, self.y + RANGE
            filtered= [s for s in SURVIVORS if  s.x > x_lower and
                                                s.x < x_upper and
                                                s.y > y_lower and
                                                s.y < y_upper and
                                                s.marked_safe == False]
            for f in filtered:
                f.marked_safe = True
                self.rescued.append(f)
                SURVIVORS.remove(f)

            time.sleep(0.5)
            self.update_position(time.time()- self._time_)
            self._time_ = time.time()

            # print(len(filtered), time.time())
            print(len(SURVIVORS), time.time()- self.init_time)
            output_file.write("%d, %f\n"%(len(SURVIVORS), time.time()- self.init_time))
