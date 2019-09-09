#retorna vetor ordenado e swaps
def selection_sort(vetor):
    pos = 0
    i = 0
    swaps = 0
    swaps_reg = []
    while i < len(vetor):
        comp = vetor[i]
        comp_pos = i
        j = i
        while j < len(vetor):
            if comp > vetor[j]:
                comp = vetor[j]
                comp_pos = j
            j+=1
            if j == len(vetor):
                if vetor[pos]!= comp and comp_pos!=pos:
                    swaps += 1
                    swaps_reg.append((comp_pos, pos))
                vetor[comp_pos], vetor[pos] = vetor[pos], comp
                pos+=1
        i+=1
    return vetor, swaps, swaps_reg