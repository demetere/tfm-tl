import os
import sys
if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
import traci

import matplotlib.pyplot as plt

STEPS = 10000

if __name__ == "__main__":

    sumoBinary = "/usr/share/sumo/bin/sumo"
    sumoCmd = [sumoBinary, "-c", "dataset/vake.sumo.cfg"]

    traci.start(sumoCmd)
    step = 0

    car_lengths  = []
    while step < STEPS:
        traci.simulationStep()
        step += 1
        car_lengths.append(len(traci.vehicle.getIDList()))

    traci.close()

    time = [i for i in range(STEPS)]
    plt.plot(time, car_lengths)
    plt.show()
