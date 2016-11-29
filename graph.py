class Vertex():
	def __init__(self, key):
		self.id = key
		self.connectedTo = []
	def addNeighbor(self, key):
		self.connectedTo.append(key)
	def __str__(self):
		return str(self.id) + "connected to " + (", ".join([x for x in self.connectedTo]) or "None")
class Graph:
	def __init__(self):
		# create a new graph
		self.vertices = []
		self.numOfVertices = 0

	def addVertex(self, vertex):
		# add a new vertex to the graph
		pass
	def addEdge(self, fromVertex, toVertex):
		# add an edge
		pass
	def addEdge(self, fromVertex, toVertex, weight):
		# add a weighted edge
		pass
	def getVertex(self, vertKey):
		# get teh vertex with the name vertexKey
		pass
	def getVertices(self):
		# get all vertices
		pass
	def __contains__(self, vertex):
		# return true if vertex is in graph, else false
		pass