import numpy as np
import numpy.matlib as nm
import matplotlib.pyplot as plt

x= 10
y= 24
height = 15


a= np.array([0,y,y,0])

w_y = nm.repmat(a,1,40/(2*x))
w_y =  np.squeeze(np.asarray(w_y))
w_y = np.array(w_y)
print(w_y)
w_x = []

for i in range(int(40/x)):
	w_x.append(i*x)
	w_x.append(i*x)

print(w_x)	
w_y = np.array(w_y) + 4
w_x = np.array(w_x) + 5
print('wx,wy',w_x,w_y)
waypoint_Air = []

waypoint_ENU = []

co = np.cos(-10*(np.pi/180.0))
si = np.sin(-10*(np.pi/180.0))

w_y_ENU = []
w_x_ENU = []

for i in range(len(w_y)):
	waypoint_Air.append([w_x[i],w_y[i],height])
	wxe = co*w_x[i]-si*w_y[i]
	wye = si*w_x[i]+co*w_y[i]
	w_x_ENU.append(wxe)
	w_y_ENU.append(wye)
	waypoint_ENU.append([wxe,wye,height])

print(waypoint_Air)
print(waypoint_ENU)

#plt.figure(0)
plt.plot(w_y,w_x)
plt.plot(w_y_ENU,w_x_ENU)
plt.show()

