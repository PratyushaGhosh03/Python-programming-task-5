from collections import Counter

def find_duplicates(lst):
    return [item for item, count in Counter(lst).items() if count > 1]

# Example usage
print(find_duplicates([1, 2, 3, 4, 2, 3, 5, 6, 1]))
