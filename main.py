import os
import sys
if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
import traci
# import libsumo as traci

sumoBinary = "/usr/share/sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "dataset/vake.sumo.cfg"]

traci.start(sumoCmd)
step = 0
while step < 20000:
    traci.simulationStep()
    step += 1

traci.close()