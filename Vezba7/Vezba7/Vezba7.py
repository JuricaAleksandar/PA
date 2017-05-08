from enum import Enum	
import numpy

class Graph:
    def __init__(self,n):
        self.cvorovi = []
        for i in range(n):
            V = Vertex(VertexColor.BLACK,None,numpy.inf,None)
            self.cvorovi.append(V)
    def add(self,id,vertex):
        self.cvorovi[id-1].append(vertex)
    def print(self,id):
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
		
graf = Graph(5)
graf.add(1,Vertex(VertexColor.WHITE, d1=2, d2=0))
graf.add(1,Vertex(VertexColor.WHITE, d1=5, d2=0))
graf.add(2,Vertex(VertexColor.WHITE, d1=1, d2=0))
graf.add(2,Vertex(VertexColor.WHITE, d1=5, d2=0))
graf.add(2,Vertex(VertexColor.WHITE, d1=4, d2=0))
graf.add(2,Vertex(VertexColor.WHITE, d1=3, d2=0))
graf.add(3,Vertex(VertexColor.WHITE, d1=2, d2=0))
graf.add(3,Vertex(VertexColor.WHITE, d1=4, d2=0))
graf.add(4,Vertex(VertexColor.WHITE, d1=2, d2=0))
graf.add(4,Vertex(VertexColor.WHITE, d1=3, d2=0))
graf.add(4,Vertex(VertexColor.WHITE, d1=5, d2=0))
graf.add(5,Vertex(VertexColor.WHITE, d1=1, d2=0))
graf.add(5,Vertex(VertexColor.WHITE, d1=2, d2=0))
graf.add(5,Vertex(VertexColor.WHITE, d1=4, d2=0))