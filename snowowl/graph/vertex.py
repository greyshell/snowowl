#!/usr/bin/env python3

# author: greyshell


class Vertex:

    def __init__(self, vertex):
        self.vertex_name = vertex
        self.neighbor_edges_obj = list()  # list is used to support self loop

    def add_neighbor_edge_obj(self, edge_obj):
        self.neighbor_edges_obj.append(edge_obj)

    def __str__(self):
        vertex_name = str(self.vertex_name)
        edges = list()
        for edge_obj in self.neighbor_edges_obj:
            neighbor = edge_obj.dst_vertex
            edges.append(str(neighbor))
        node = {vertex_name: edges}
        return str(node)
