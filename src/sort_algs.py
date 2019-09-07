import copy
#retorna vetor ordenado e swaps
def insertion_sort(vetor):
    pos = 0
    i = 0
    swaps = 0
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
                if vetor[pos]!= comp:
                    swaps += 1
                vetor[comp_pos], vetor[pos] = vetor[pos], comp

                pos+=1
        i+=1
    print('hehehe')
    print(vetor, swaps)
    return vetor, swaps
insertion_sort([5,6,7,8,4,1,2,3,9])