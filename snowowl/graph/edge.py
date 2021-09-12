#!/usr/bin/env python3

# author: greyshell


class Edge:

    def __init__(self, src_vertex, dst_vertex, weight):
        self.src_vertex = src_vertex
        self.dst_vertex = dst_vertex
        self.weight = weight

    def __eq__(self, other_obj):
        # compare based on weight
        return self.weight == other_obj.weight

    def __lt__(self, other_obj):
        # compare based on weight
        return self.weight < other_obj.weight

    def __gt__(self, other_obj):
        # compare based on weight
        return self.weight > other_obj.weight

    def __str__(self):
        edge = list()
        edge.append(self.src_vertex)
        edge.append(self.dst_vertex)
        edge.append(self.weight)
        return str(edge)
