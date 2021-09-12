#!/usr/bin/env python3

# author: greyshell
# description: Graph ADT

from .edge import Edge
from .vertex import Vertex

__all__ = ['UndirectedGraph']


class UndirectedGraph:

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)

    def get_vertex_obj(self, vertex):
        return self.vertices.get(vertex, False)

    def get_all_vertices(self):
        # self.vertices.keys returns <class 'dict_keys'> thus converting that to list
        return list(self.vertices.keys())

    def add_edge(self, src_vertex, dst_vertex, weight=0):
        if src_vertex not in self.vertices:
            self.add_vertex(src_vertex)

        if dst_vertex not in self.vertices:
            self.add_vertex(dst_vertex)

        src_vertex_obj = self.vertices[src_vertex]
        dst_vertex_obj = self.vertices[dst_vertex]

        src_vertex_obj.add_neighbor_edge_obj(Edge(src_vertex, dst_vertex, weight))
        # undirected graph -> add a backward edge
        dst_vertex_obj.add_neighbor_edge_obj(Edge(dst_vertex, src_vertex, weight))

    def get_all_edges(self):
        """
        time complexity: O(V + E)
        :return: list[list]
        """
        total_edges = list()
        for vertex_obj in self.vertices.values():
            for edge_obj in vertex_obj.neighbor_edges_obj:
                src_vertex = edge_obj.src_vertex
                dst_vertex = edge_obj.dst_vertex
                weight = edge_obj.weight

                # prepare backward edge
                backward_edge = [dst_vertex, src_vertex, weight]
                if backward_edge not in total_edges:
                    total_edges.append([src_vertex, dst_vertex, weight])
        return total_edges

    def __str__(self):
        g = list()
        for vertex_obj in self.vertices.values():
            g.append(vertex_obj.__str__())
        return str(g)
