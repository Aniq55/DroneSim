# DroneSim
A real-time simulator using the example of an aerial swarm of drones in a
survivor rescue scenario with the help of common Python libraries.

## Scenario
```
Swarm of Drones (UAV)			nD
Detect ground survivors		nS
Rescue them
Fixed range							  R
Fixed test area					  L x L
Random distribution
Random walk by drones
```

## Solution
```
Class for UAV							UAV.py
Class for Survivors					survivor.py
Functions for chaos					chaos.py
Define constants						constants.py
Global variables						constants.py
Real-time simulation				main.py
Plotting the results					plotter.py
```

### UAV class
```
Data members:
ID							unique identity
position				x, y
velocity				velx, vely
rescued					list of survivors rescued
_time_					to measure time
Init_time				time of initialization
```

```
Functions:
__init__					Initialize
update_position		Move the UAV
search_survivors	Search for survivors
```

### Survivor class
```
Data members:
ID								unique identity
position					x, y
marked_safe				whether rescued
```

### Randomness
```
random_pos():
random.uniform(0, L)

random_val():
random.uniform(-10.0, 10.0)
```

### Random walk mobility of UAVs
```
update_position(time_elapsed):
  x = (x + velx* time_elapsed* random_val() )%L
  y = (y + vely* time_elapsed* random_val() )%L
```

### Searching for Survivors
```
search_survivors():
  init_time = time()
  While search is not complete:
  Mark safe the survivors in range
  Time delay (for rescue)
  update_position( time() - _time_ )
  _time_ = time()
  Write data to file
```

### Defining Global variables
```
DRONES			List of drone objects
SURVIVORS		List of survivor objects
missions			List of parallel threads
output_file		File for logging output
```

### Creating objects
```
for i in range(nD):
DRONES.append( UAV(i, random_pos(), random_pos(), Vmax, Vmax )

for i in range(nS):
SURVIVORS.append( survivor(i, random_pos(), random_pos() )
```

### Running Parallel threads
```
for i in range(nD):
  process = threading.Thread( target=DRONES[i].search_survivors(), args=None )
  process.start()
  missions.append(process)
```

### Extracting results
```
search_survivors():
  ...
  While search is not complete:
  ...
  ...
  output_file.write("%d, %f\n"%( len(SURVIVORS),time.time()- self.init_time) )
```

### Visual Representation
```
import matplotlib.pyplot as plt
f = open(‘out.txt’, ‘r’)
N, T = [], []
for line in f:
  l = line.split(‘,’)
  N.append(int(l[0]))
  T.append(float(l[1]))
plt.plot(T,N)
plt.show()
```
