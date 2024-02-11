def rabin_karp(text, pattern):
    n = len(text) # O(1)
    m = len(pattern) # O(1)

    if n < m:
        return  # Tidak mungkin menemukan pola jika panjang pola lebih besar dari teks

    hash_table = { # O(1) tetap
        'A': 0,
        'G': 1,
        'C': 2,
        'T': 3
    }

    # Hitung nilai hash untuk pola
    pattern_hash = 0
    for i in range(m): # O(m)
        pattern_hash = pattern_hash * 4 + hash_table[pattern[i]] # O(1)
        # print(pattern_hash)

    print(f'Pattern value: {pattern_hash}\n')

    # Hitung nilai hash untuk semua substring
    text_hashes = []
    # ruang : O(n-m+1)

    # semua hash funct dihitung dalam kompleksitas O(1) dengan operasi matematis tanpa melibatkan loop
    text_hash = 0
    for i in range(m): # O(m)
        text_hash = text_hash * 4 + hash_table[text[i]]
    text_hashes.append(text_hash)

    for i in range(1, n - m + 1): # O(n-m) hitung semua hash untuk setiap substring sepanjang pattern
        # Hitung nilai hash untuk substring berikutnya di teks
        text_hash = (text_hash - hash_table[text[i - 1]] * 4**(m - 1)) * 4 + hash_table[text[i + m - 1]] # O(1)
        text_hashes.append(text_hash)
    # print(text_hashes)

    for i in range(n - m + 1): # O(m(n-m))
        # Cocokkan nilai hash, jika cocok, periksa substring secara lebih mendalam
        print(f'Iterasi {i+1}. substring: {text[i:i + m]}, value = {text_hashes[i]}.') # O(m)
        if pattern_hash == text_hashes[i]: # cek O(1)
            print("Pattern is found!\n")

    return  #O(mn) => tepatnya adalah O(m(n-m)), dimana n <= m

# Test Pattern ditemukan
genome = 'AGTCGTTAGAT'
pattern = 'CGTTA'
rabin_karp(genome, pattern)
expected = "Pattern found at value = 636."


