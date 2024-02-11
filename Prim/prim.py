import heapq

def feasible(mst_vertex, adj_list):
    # feasible artinya jika titik dipilih tidak akan menimbulkan siklus dan tidak mengunjungi titik yang sudah ada
    # feasible_edge_lst artinya kumpulan calon titik yang bisa dipilih
    feasible_edge_lst = []
    for vertex in mst_vertex:
        for edge in adj_list[vertex]:
            if edge[0] not in mst_vertex:
                feasible_edge_lst.append([edge[1], vertex, edge[0]])
    # print(feasible_edge_lst)
    return feasible_edge_lst


def min_edge_search(feasible_edge_lst):
    min_edge = feasible_edge_lst[0]
    for edge in feasible_edge_lst:
        if edge[0] < min_edge[0]:
            min_edge = edge
    return min_edge


def Prim(n, adj_list, start):  # O(VE), dimana V adalah jumlah titik dan E adalah jumlah sisi/edge
    mst_vertex = [start]
    mst_edge = []
    mst_cost = 0

    for i in range(1, n):  # jumlah MST_edge pasti = n - 1
        feasible_edge = feasible(mst_vertex, adj_list)
        min_edge = min_edge_search(feasible_edge)  # ini karena min edge butuh untuk mencari sebanyak E
        print(f'Iteration #{i}: adding the edge ({min_edge[1]}, {min_edge[2]}) with weigth {min_edge[0]}.')
        mst_vertex.append(min_edge[2])
        mst_edge.append(
            (min_edge[1], min_edge[2]))
        mst_cost += min_edge[0]

    print()
    return mst_cost, mst_edge


def Prim_PrioQueue(n, adj_list, start):  # V log E
    mst_vertex = [start]
    mst_edge = []
    mst_cost = 0
    priority_queue = []  # sedangkan dengan prio queue mencari sisi adalah sebanyak log E saja
    count = 1

    for edge in adj_list[start]:
        heapq.heappush(priority_queue, (edge[1], start, edge[0]))  # push edge dengan weight sebagai prioritas ke heapq

    print(priority_queue)

    while len(mst_vertex) != n:
        min_edge = heapq.heappop(priority_queue)  # pop edge terkecil dari prio queue
        if min_edge[2] not in mst_vertex:  # vertex yang dipilih adalah vertex yang belum ada di mst_vertex lst
            print(f'Iteration #{count}: adding the edge ({min_edge[1]}, {min_edge[2]}) with weigth {min_edge[0]}.')
            count += 1
            mst_vertex.append(min_edge[2])  # menambah vertex tujuan ke mst_vertex
            mst_edge.append((min_edge[1], min_edge[2], min_edge[0]))
            mst_cost += min_edge[0]
            for edge in adj_list[min_edge[2]]:  # for edge di adj_list dengan key tujuan yang dipilih
                if edge[0] not in mst_vertex:  # kalau vertex belum ada di mst_vertex, maka akan dipilih
                    heapq.heappush(priority_queue, (
                        edge[1], min_edge[2], edge[0]))  # push edge dengan weight sebagai prioritas ke heapq

    print(priority_queue)
    return mst_cost, mst_edge


if __name__ == '__main__':
    # test case pastikan jika ada edge yang bobotnya sama masih bisa dipilih yang benar
    adj_list = {
        0: [[1, 9], [2, 5], [4, 8]],
        1: [[0, 9], [3, 7], [4, 10], [6, 11]],
        2: [[0, 5], [3, 7], [4, 7], [5, 5]],
        3: [[1, 7], [2, 7], [4, 4], [5, 4]],
        4: [[0, 8], [1, 10], [2, 7], [3, 4], [5, 4]],
        5: [[2, 5], [3, 4], [4, 4], [7, 13]],
        6: [[1, 11], [7, 1]],
        7: [[5, 13], [6, 1]]
    }

    adj_list_ppt = {'A': [['B', 9], ['E', 8], ['C', 5]],
                    'B': [['A', 9], ['E', 10], ['D', 7], ['G', 11]],
                    'C': [['A', 5], ['E', 7], ['D', 7], ['F', 5]],
                    'D': [['B', 7], ['E', 4], ['C', 7], ['F', 4]],
                    'E': [['A', 8], ['B', 10], ['C', 7], ['D', 4], ['F', 4]],
                    'F': [['E', 4], ['D', 4], ['H', 13], ['C', 5]],
                    'G': [['B', 11], ['H', 1]],
                    'H': [['G', 1], ['F', 13]]}

    mst_cost, mst_edge = Prim(8, adj_list_ppt, 'H')
    # mst_cost, mst_edge = Prim(8, adj_list, 0)
    Prim_PrioQueue(8, adj_list_ppt, 'H')
    print()
    # Prim_PrioQueue(8, adj_list, 0)

    # if printing all the iteration progress:

    # Iteration #1: adding the edge (0, 2) with weigth 5.
    # Iteration #2: adding the edge (2, 5) with weigth 5.
    # Iteration #3: adding the edge (5, 3) with weigth 4.
    # Iteration #4: adding the edge (3, 4) with weigth 4.
    # Iteration #5: adding the edge (3, 1) with weigth 7.
    # Iteration #6: adding the edge (1, 6) with weigth 11.
    # Iteration #7: adding the edge (6, 7) with weigth 1.

    # The output should be:
    # 37
    # {(3, 1, 7), (2, 5, 5), (1, 6, 11), (6, 7, 1), (0, 2, 5), (5, 3, 4), (3, 4, 4)}
