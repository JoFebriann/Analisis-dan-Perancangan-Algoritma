from collections import defaultdict
import heapq


# MST dari sebuah graf terhubung tidak selalu bersifat unik, artinya mungkin terdapat
# banyak pilihan MST yang memiliki total bobot sisi yang sama-sama minimal.
# Dalam variasi ini, kita akan menyortir kembali berbagai pilihan MST tersebut (jika terdapat lebih dari 1 solusi) dan
# kita akan memilih MST yang ketinggiannya (levelnya) paling kecil.

# Dari graf yang diinputkan, akan dipilih MST dengan total bobot yang terkecil.
# Jika masih terdapat banyak pilihan MST dengan bobot terkecil,
# maka kita akan mengambil MST dengan ketinggian paling kecil (yaitu panjang lintasan dari titik akar ke titik daun yang paling dalam).

# N = titik pada graf
# M = sisi pada graf

def build_adj_list(edge_list):
    adj_list = defaultdict(list)

    for u, v, w in edge_list:
        adj_list[u].append([v, w])
        adj_list[v].append([u, w])

    return dict(adj_list)


def Prim(n, adj_list, start):
    mst_vertex = [start]
    mst_edge = []
    mst_cost = 0
    priority_queue = []
    eksentrisitas = 0
    height_dict = {start: 0}
    counter = 0

    for edge in adj_list[start]:
        heapq.heappush(priority_queue, (edge[1], counter, start, edge[0]))
        counter += 1

    while len(mst_vertex) != n:
        min_edge = heapq.heappop(priority_queue)
        if min_edge[3] not in mst_vertex:
            mst_vertex.append(min_edge[3])
            mst_edge.append((min_edge[3], min_edge[2]))
            mst_cost += min_edge[0]
            height_dict[min_edge[3]] = height_dict[min_edge[2]] + 1
            eksentrisitas = max(eksentrisitas,
                                height_dict[min_edge[3]])
            for edge in adj_list[min_edge[3]]:
                if edge[0] not in mst_vertex:
                    heapq.heappush(priority_queue, (
                        edge[1], counter, min_edge[3],
                        edge[0]))
                    counter += 1

    print('height_dict', height_dict)
    return mst_cost, mst_edge, eksentrisitas


def Prim2(n, adj_list, start):
    mst_vertex = set([start])
    mst_edge = []  # MST
    mst_cost = 0  # weight
    priority_queue = []
    eksentrisitas = 0
    height_dict = {start: 0}
    counter = 0

    for edge in adj_list[start]:
        heapq.heappush(priority_queue, (edge[1], counter, start, edge[0]))
        counter += 1

    while len(mst_vertex) != n:
        min_edge = heapq.heappop(priority_queue)
        if min_edge[3] not in mst_vertex:
            mst_vertex.add(min_edge[3])
            mst_edge.append((min_edge[3], min_edge[2]))
            mst_cost += min_edge[0]
            height_dict[min_edge[3]] = height_dict[min_edge[2]] + 1
            eksentrisitas = max(eksentrisitas, height_dict[min_edge[3]])
            for edge in adj_list[min_edge[3]]:
                if edge[0] not in mst_vertex:
                    heapq.heappush(priority_queue, (edge[1], counter, min_edge[3], edge[0]))
                    counter += 1

    return mst_cost, mst_edge, eksentrisitas


def test_if_all_the_edge_are_same_weight():
    edge_list1 = [
        ['A', 'B', 1],
        ['A', 'C', 1],
        ['B', 'C', 1],
        ['B', 'D', 1],
        ['D', 'C', 1],
        ['D', 'E', 1],
        ['C', 'E', 1]
    ]

    adj_list1 = {'A': [['B', 1], ['C', 1]],
                 'B': [['A', 1], ['C', 1], ['D', 1]],
                 'C': [['A', 1], ['B', 1], ['D', 1], ['E', 1]],
                 'D': [['B', 1], ['C', 1], ['E', 1]],
                 'E': [['D', 1], ['C', 1]]}

    print(len(adj_list1))
    # mst_cost, mst_edge, eccentricity = Prim(len(adj_list1), adj_list1, 'A')
    assert Prim2(len(adj_list1), adj_list1, 'A') == (4, [('B', 'A'), ('C', 'A'), ('D', 'B'), ('E', 'C')], 2)
    # print((mst_cost, mst_edge, eccentricity))
    # print("MST cost:", mst_cost)
    # print("MST edges:", mst_edge)
    # print("Eccentricity of the root:", eccentricity)


def test_complete_graph_with_all_same_weight():
    edge_list1 = [['A', 'B', 1], ['A', 'C', 1], ['A', 'D', 1], ['A', 'E', 1],
                  ['B', 'C', 1], ['B', 'D', 1], ['B', 'E', 1],
                  ['C', 'D', 1], ['C', 'E', 1],
                  ['D', 'E', 1]]

    # print(build_adj_list(edge_list1))
    adj_list1 = {'A': [['B', 1], ['C', 1], ['D', 1], ['E', 1]],
                 'B': [['A', 1], ['C', 1], ['D', 1], ['E', 1]],
                 'C': [['A', 1], ['B', 1], ['D', 1], ['E', 1]],
                 'D': [['A', 1], ['B', 1], ['C', 1], ['E', 1]],
                 'E': [['A', 1], ['B', 1], ['C', 1], ['D', 1]]}

    # mst_cost, mst_edge, eccentricity = Prim(len(adj_list1), adj_list1, 'E')
    assert Prim2(len(adj_list1), adj_list1, 'A') == (4, [('B', 'A'), ('C', 'A'), ('D', 'A'), ('E', 'A')], 1)
    assert Prim2(len(adj_list1), adj_list1, 'B') == (4, [('A', 'B'), ('C', 'B'), ('D', 'B'), ('E', 'B')], 1)
    assert Prim2(len(adj_list1), adj_list1, 'C') == (4, [('A', 'C'), ('B', 'C'), ('D', 'C'), ('E', 'C')], 1)
    assert Prim2(len(adj_list1), adj_list1, 'D') == (4, [('A', 'D'), ('B', 'D'), ('C', 'D'), ('E', 'D')], 1)
    assert Prim2(len(adj_list1), adj_list1, 'E') == (4, [('A', 'E'), ('B', 'E'), ('C', 'E'), ('D', 'E')], 1)
    #
    # print((mst_cost, mst_edge, eccentricity))
    # print("MST cost:", mst_cost)
    # print("MST edges:", mst_edge)
    # print("Eccentricity of the root:", eccentricity)


def test_complete_graph_with_different_weight():
    edge_list1 = [['A', 'B', 1], ['A', 'C', 2], ['A', 'D', 3], ['A', 'E', 4],
                  ['B', 'C', 1], ['B', 'D', 1], ['B', 'E', 1],
                  ['C', 'D', 1], ['C', 'E', 1],
                  ['D', 'E', 1]]

    # print(build_adj_list(edge_list1))
    adj_list1 = {'A': [['B', 1], ['C', 2], ['D', 3], ['E', 4]],
                 'B': [['A', 1], ['C', 1], ['D', 1], ['E', 1]],
                 'C': [['A', 2], ['B', 1], ['D', 1], ['E', 1]],
                 'D': [['A', 3], ['B', 1], ['C', 1], ['E', 1]],
                 'E': [['A', 4], ['B', 1], ['C', 1], ['D', 1]]}

    # mst_cost, mst_edge, eccentricity = Prim(len(adj_list1), adj_list1, 'A')
    assert Prim2(len(adj_list1), adj_list1, 'A') == (4, [('B', 'A'), ('C', 'B'), ('D', 'B'), ('E', 'B')], 2)

    # print((mst_cost, mst_edge, eccentricity))
    # print("MST cost:", mst_cost)
    # print("MST edges:", mst_edge)
    # print("Eccentricity of the root:", eccentricity)


def test_complete_graph_with_different_weight2():
    edge_list1 = [['A', 'B', 5], ['A', 'C', 2], ['A', 'D', 3], ['A', 'E', 4],
                  ['B', 'C', 1], ['B', 'D', 1], ['B', 'E', 1],
                  ['C', 'D', 1], ['C', 'E', 1],
                  ['D', 'E', 1]]

    # print(build_adj_list(edge_list1))
    adj_list1 = {'A': [['B', 5], ['C', 2], ['D', 3], ['E', 4]],
                 'B': [['A', 5], ['C', 1], ['D', 1], ['E', 1]],
                 'C': [['A', 2], ['B', 1], ['D', 1], ['E', 1]],
                 'D': [['A', 3], ['B', 1], ['C', 1], ['E', 1]],
                 'E': [['A', 4], ['B', 1], ['C', 1], ['D', 1]]}

    # mst_cost, mst_edge, eccentricity = Prim(len(adj_list1), adj_list1, 'A')
    assert Prim2(len(adj_list1), adj_list1, 'A') == (5, [('C', 'A'), ('B', 'C'), ('D', 'C'), ('E', 'C')], 2)

    # print((mst_cost, mst_edge, eccentricity))
    # print("MST cost:", mst_cost)
    # print("MST edges:", mst_edge)
    # print("Eccentricity of the root:", eccentricity)


def test_if_all_the_edge_are_same_weight_2():
    edge_list1 = [
        ['A', 'B', 1],
        ['A', 'C', 1],
        ['B', 'C', 1],
        ['B', 'D', 1],
        ['D', 'C', 1],
        ['D', 'E', 1],
        ['C', 'E', 1]
    ]

    # print(build_adj_list(edge_list1))
    adj_list1 = {'A': [['B', 1], ['C', 1]],
                 'B': [['A', 1], ['C', 1], ['D', 1]],
                 'C': [['A', 1], ['B', 1], ['D', 1], ['E', 1]],
                 'D': [['B', 1], ['C', 1], ['E', 1]],
                 'E': [['D', 1], ['C', 1]]}

    # mst_cost, mst_edge, eccentricity = Prim(len(adj_list1), adj_list1, 'C')
    print()
    assert Prim2(len(adj_list1), adj_list1, 'C') == (4, [('A', 'C'), ('B', 'C'), ('D', 'C'), ('E', 'C')], 1)
    # print((mst_cost, mst_edge, eccentricity))
    # print("MST cost:", mst_cost)
    # print("MST edges:", mst_edge)
    # print("Eccentricity of the root:", eccentricity)


def test():
    test_if_all_the_edge_are_same_weight()
    test_if_all_the_edge_are_same_weight_2()
    test_complete_graph_with_all_same_weight()
    test_complete_graph_with_different_weight()
    test_complete_graph_with_different_weight2()


if __name__ == '__main__':
    test()

    N = 6
    edge_list = [
        [0, 1, 8],
        [0, 2, 6],
        [0, 3, 3],
        [1, 3, 3],
        [1, 5, 5],
        [2, 3, 2],
        [2, 4, 2],
        [2, 5, 4],
        [3, 4, 1],
        [3, 5, 2],
        [4, 5, 2]
    ]

    R = 3
    adj_list = {0: [[1, 8], [2, 6], [3, 3]],
                1: [[0, 8], [3, 3], [5, 5]],
                2: [[0, 6], [3, 2], [4, 2], [5, 4]],
                3: [[0, 3], [1, 3], [2, 2], [4, 1], [5, 2]],
                5: [[1, 5], [2, 4], [3, 2], [4, 2]],
                4: [[2, 2], [3, 1], [5, 2]]}

    mst_cost, mst_edge, max_depth = Prim(len(adj_list), adj_list, R)
    print("MST cost:", mst_cost)
    print("MST edges:", mst_edge)
    print("Eccentricity of the root:", max_depth)
    print()

    adj_list_ppt = {'A': [['B', 9], ['E', 8], ['C', 5]],
                    'B': [['A', 9], ['E', 10], ['D', 7], ['G', 11]],
                    'C': [['A', 5], ['E', 7], ['D', 7], ['F', 5]],
                    'D': [['B', 7], ['E', 4], ['C', 7], ['F', 4]],
                    'E': [['A', 8], ['B', 10], ['C', 7], ['D', 4], ['F', 4]],
                    'F': [['E', 4], ['D', 4], ['H', 13], ['C', 5]],
                    'G': [['B', 11], ['H', 1]],
                    'H': [['G', 1], ['F', 13]]}

    mst_cost, mst_edge, max_depth = Prim2(len(adj_list_ppt), adj_list_ppt, 'H')
    print("MST cost:", mst_cost)
    print("MST edges:", mst_edge)
    print("Eccentricity of the root:", max_depth)
