import vrep
import time

vrep.connect()
#vrep.getSensors()
#vrep.setRightSpeed(0.1)
#vrep.setLeftSpeed(0.1)

while True:
    dist = vrep.getSensors()

    #daqui
    if dist[0] <= 0.2872 or dist[1] <= 0.2872 or dist[2] <= 0.2872:
        vrep.setRightSpeed(0)
        vrep.setLeftSpeed(1)
    else:
        vrep.setRightSpeed(1)
        vrep.setLeftSpeed(1)
    print dist
    # ate aqui

    time.sleep(0.005)

time.sleep(1)
vrep.disconnect()
