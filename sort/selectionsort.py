def selection_sort(A): 
    for i in range(len(A)): 
        minimum = i 
        for j in range(i+1, len(A)): 
            if A[minimum] > A[j]: 
                minimum = j 
        A[i], A[minimum] = A[minimum], A[i] 
    return A
A = [12,3,2,123,77,9] 
print(selection_sort(A))