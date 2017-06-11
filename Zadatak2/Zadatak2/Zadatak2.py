from enum import Enum	
import numpy

class Graf:
    def __init__(self,n):
        self.cvorovi = []
        for i in range(n):
            V = Vertex(VertexColor.BLACK,None,numpy.inf,None)
            self.cvorovi.append(V)
    def add(self,id,vertex):
        self.cvorovi[id-1].append(vertex)
    def printGraph(self,id):
        print("Cvor " + str(id) + ", susedi: ")
        for i in range(len(self.cvorovi[id-1])):
            print(self.cvorovi[id-1][i].d1)

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		