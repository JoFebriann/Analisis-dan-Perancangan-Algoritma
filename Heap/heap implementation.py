def Parent(v):
    if v == 1:
        return
    parent_idx = v // 2
    return parent_idx


def Leaf(v, H):
    l = len(H) - 1

    if 2 * v <= l:
        left_leaf = 2 * v
    else:
        left_leaf = None

    if 2 * v + 1 <= l:
        right_leaf = 2 * v + 1
    else:
        right_leaf = None

    return left_leaf, right_leaf


def swap(a, b, H):
    H[a], H[b] = H[b], H[a]


def BottomUpParentDominance(v, H):  # v is child
    if v > 0:
        if v == 1:  # v is root, parental dominance achieved already
            return
        Par_idx = Parent(v)
        if H[v] >= H[Par_idx]:  # not ParentalDominance(Par, v):
            swap(Par_idx, v, H)
            BottomUpParentDominance(Par_idx, H)
        return
    else:
        print('invalid v')


def TopDownParentDominance(v, H):  # v is parrent
    LC, RC = Leaf(v, H)
    # print(LC, RC)
    if (LC is None) and (RC is None):  # parental dominance achieved already
        return

    # Kondisi hanya ada 1 child
    if LC is None:
        if H[RC] > H[v]:
            swap(v, RC, H)
            TopDownParentDominance(RC, H)

    elif RC is None:
        if H[LC] > H[v]:
            swap(v, LC, H)
            TopDownParentDominance(LC, H)

    else:  # Kondisi child 2
        if H[LC] > H[RC]:  # Left child  is greater than Right Child
            if H[LC] > H[v]: # Left child  is greater than parent
                # print(1, '|', H[v], H[LC])
                swap(v, LC, H)
                TopDownParentDominance(LC, H)
        elif H[LC] < H[RC]:  # Right child is greater than Left Child
            if H[RC] > H[v]:  # Right child  is greater than parent
                # print(2, '|', H[v], H[RC])
                swap(v, RC, H)
                TopDownParentDominance(RC, H)
    return

def Heapify(H):
    l = len(H) - 1
    temp = l // 2 + 1

    for i in range(1, l // 2 + 1):
        temp -= 1
        # print(temp)
        TopDownParentDominance(temp, H)
    return




if __name__ == '__main__':
    # H = [None, 8, 4, 6, 2, 3, 5, 0, 1, 7]
    # H = [None, 8, 4, 6, 7, 5, 3, 3, 9]
    # v = 8
    # print(H)
    # BottomUpParentDominance(v, H)
    # print(H)

    # H = [None, 2, 7, 6, 4, 3, 5, 0, 8, 1]
    # v = 1
    # print(H)
    # TopDownParentDominance(v, H)
    # print(H)

    H = [None, 5, 1, 8, 7, 4, 3, 2, 0, 9, 6]
    print(H)
    Heapify(H)
    print(H)

