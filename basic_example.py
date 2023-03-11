from serial.tools import list_ports

import mypydobot
import time

def start_dobot():
	available_ports = list_ports.comports()
	print(f'available ports: {[x.device for x in available_ports]}')
	port = available_ports[0].device

	device = mypydobot.Dobot(port=port, verbose=True)

	(x, y, z, r, j1, j2, j3, j4) = device.pose()
	print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

	try:   
		time.sleep(1)
		device.move_to(x + 20, y, z, r, wait=True)
		device.motor(0,30)
		device.wait(50000)
		time.sleep(5)    
		device.move_to(x, y, z, r, wait=True)
		device.motor(0,0)
		time.sleep(5)

		device.close() 

	except KeyboardInterrupt:   # exceptに例外処理を書く
		print('stop!')




