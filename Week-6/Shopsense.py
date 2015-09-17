class Coordinates(object):
	"""
	Denotes a point in 2-D plane

	"""
	def __init__(self, x , y) :
		self.x = x
		self.y = y 
	
	def getX():
		return self.x

	def getY() :
		return self.y

	def manhattanDistance(self, other) :
		return  abs(self.x - other.x) + abs(self.y - other.y)


print(3//2)
print()
N , M , D = raw_input().split(' ')
N, M, D = int(N), int(M), int(D)
locations = []
for i in range(N) :
	x, y = raw_input.split(' ')
	x, y = int(x), int(y)
	locations.append(Coordinates(x, y))


#locations.append(Coordinates(2, 2))
#locations.append(Coordinates(3, 3))
targets = []
for i in range(M) :
	x, y = raw_input.split(' ')
	x, y = int(x), int(y)
	targets.append(Coordinates(x, y))
#targets.append(Coordinates(1, 0))
#targets.append(Coordinates(0, 0))
#targets.append(Coordinates(2, 0))
count = 0
for location in locations :
	for target in targets :
		if target.manhattanDistance(location) <= D :
			count += 1
if count > (len(targets)//2) :
	print("YES")




