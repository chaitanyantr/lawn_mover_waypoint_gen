#!/usr/bin/env python


arena_length = 40 # Meters
arena_bredth = 30 # Meters

offset_length = 5 # Meters
offset_bredth = 5 # Meters

pattern_length =  arena_length - offset_length
pattern_bredth =  arena_bredth - offset_bredth

waypointx = []
waypointy = []

count = 0
n_w = []
m_w = []

def main():

	print('dl',n_w)	

	for x in range(pattern_length):
		for y in range(pattern_bredth):
			if x == 24 or x == 0:

				if y % 5 == 0:

					waypointx.append(x)
					waypointy.append(y)

					
	print(waypointx,waypointy)
	tl = len(waypointx)

	print('tl',tl)
	
	f = waypoint[0:len(waypoint)/2]
	l = waypoint[len(waypoint)/2:]
	
	print(f,l)

	f.pop(0)

	for x,y in zip(range(0,(len(waypoint)/2),2),range(2,(len(waypoint)/2),2)):

		j = l[x:y]

		n_w.append(j)

		s = f[x:y]

		n_w.append(s)

		print('n_w',n_w)

		print('t1',n_w[0])

		print('t2',n_w[0][0])


	for k in range(len(waypoint)):
		m_w.insert(k,0)


	for p in range(0,(len(waypoint)/2)-1,2):
		m_w.insert(p,n_w[p][1])
	

	print('as',m_w)



if __name__ == '__main__':
	main()