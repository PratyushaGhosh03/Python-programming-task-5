import heapq

def find_k_largest(lst, k):
    return heapq.nlargest(k, lst)

# Example usage
print(find_k_largest([3, 1, 4, 1, 5, 9, 2, 6, 5], 3))
