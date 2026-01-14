
from pprint import pprint
from collections import deque



def graph_representation():
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A','C', 'E']
    graph['C'] = ['A', 'B', 'E', 'F']
    graph['E'] = ['B', 'C']
    graph['F'] = ['C']
    matrix_elements = sorted(graph.keys())
    cols = rows = len(matrix_elements)

    adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
    edges_list = []

    for key in matrix_elements:
        for neighbor in graph[key]:
            edges_list.append((key, neighbor))
    
    pprint(adjacency_matrix)
    pprint(edges_list)

    for edge in edges_list:
        index_first_vertex = matrix_elements.index(edge[0])
        index_second_vertex = matrix_elements.index(edge[1])
        adjacency_matrix[index_first_vertex][index_second_vertex] = 1
    
    pprint(adjacency_matrix)



def build_graph_for_breadth():
    graph = dict()
    graph['A'] = ['B', 'D', 'G']
    graph['B'] = ['A', 'E', 'F']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'C', 'D']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']
    
    return graph


def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque(root)
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adjacent_nodes = graph[node]

        remaining_elements = set(adjacent_nodes).difference(set(visited_vertices))
        
        if (len(remaining_elements)) > 0:
            for element in sorted(remaining_elements):
                visited_vertices.append(element)
                graph_queue.append(element)
    
    return visited_vertices


def build_graph_for_depth():
    graph = {}
    graph['A'] = ['B', 'S']
    graph['B'] = ['A']
    graph['S'] = ['A', 'G', 'C']
    graph['D'] = ['C']
    graph['G'] = ['S', 'F', 'H']
    graph['H'] = ['G', 'E']
    graph['E'] = ['H', 'C']
    graph['F'] = ['G', 'C']
    graph['C'] = ['D', 'S', 'E', 'F']

    return graph


def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = []

    graph_stack.append(root)
    node = root

    while graph_stack:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adjacent_nodes = graph[node]
        if set(adjacent_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adjacent_nodes).difference(set(visited_vertices))

        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node
    
    return visited_vertices
    

if __name__ == "__main__":
    # graph_representation()
    # print(breadth_first_search(build_graph_for_breadth(), "B"))
    print(depth_first_search(build_graph_for_depth(), "A"))





