# Implementasikan Algoritma Quick Sort dengan efisiensi waktu rata-rata O(n log n) dan efisiensi ruang O(n log n)
import random


def generate_random_list(n):
    return [random.randint(1, 100) for _ in range(n)]


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    i = 1
    j = len(lst) - 1

    while i <= j:  # stopping criterion i >= j
        # partisi kiri: <= pivot
        # partisi kanan: >= pivot
        if lst[i] >= pivot:
            if lst[j] <= pivot:
                (lst[i], lst[j]) = (lst[j], lst[i])  # swap
            j -= 1
        else:
            i += 1

    (lst[0], lst[j]) = (lst[j], lst[0])
    return quick_sort(lst[:j]) + [pivot] + quick_sort(lst[j + 1:])


if __name__ == '__main__':
    lst2 = [3, 2, 9, 4, 8, 7, 1, 5, 6]
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst0 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    lst1 = generate_random_list(100)
    # print(lst2)
    print(lst)
    print()
    # print()
    print(quick_sort(lst0))

'''
Analisis efisiensi waktu rata-rata O(n log n) dan efisiensi ruang O(n log n)

Efisiensi waktu (teta(n log n)):
Efisiensi waktu didapat dari fungsi rekursif yang selalu membagi masalah berukuran n menjadi 2 submasalah berukuran n/2, 
dengan catatan pivot hanya berukuran 1 sehingga langsung di return (tidak masuk operasi dasar),
kemudian menggabungkan nya membutuhkan teta(n) operasi jadi dengan rumus efesiensi waktu bla bla (di ppt)
efisiensi waktu rata rata nya menjadi teta(n log n)

Efisiensi ruang (O(n)) 
Efisiensi ruang didapat dari perhitungan setiap pemanggilan rekursif, 
dimana setiap rekursif dijalankan akan dibuat temporary list baru untuk partisi kanan, kiri, dan pivotnya 
maka efesiensi ruangnya setara dengan kedalam stack rekursifnya
yaitu O(n) dimana n adalah jumlah elemen dalam list
dengan average case nya O(log n)  

O(n) < O(n log n) 

'''
