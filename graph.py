class Vertex():
	def __init__(self, key):
		self.id = key
		self.connectedTo = []
	def addNeighbor(self,key):
		self.connectedTo.append(key)
	def __str__(self):
		return str(self.id) + "connected to " + ", ".join([x for x in self.connectedTo])
	def getConnections(self):
		return self.connectedTo
	def getId(self):
		return self.id

class Graph:
	def __init__(self):
		# create a new graph
		self.vertices = {}
		self.numOfVertices = 0

	def addVertex(self, vertex):
		# add a new vertex to the graph
		newVertex = Vertex(vertex)
		self.vertices[vertex] = newVertex
		self.numOfVertices += 1
		return newVertex

	def addEdge(self, fromVertex, toVertex):
		# add a weighted edge
		if fromVertex not in self.vertices:
			nv = self.addVertex(fromVertex)
		if toVertex not in self.vertices:
			nv = self.addVertex(toVertex)
		self.vertices[fromVertex].addNeighbor(self.vertices[toVertex])

	def getVertex(self, vertKey):
		# get the vertex with the name vertexKey
		if vertKey in self.vertices:
			return self.vertices[vertKey]
		else:
			return None

	def getVertices(self):
		# get all vertices
		return self.vertices.keys()

	def __contains__(self, vertex):
		# return true if vertex is in graph, else false
		return vertex in self.vertices.keys()

	def __iter__(self):
		# Iterate over all vertices objects in graph
		return iter(self.vertices.values())