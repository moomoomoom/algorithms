from decimal import Decimal

def merge(left, right):
    index_l = 0
    index_r = 0
    result = []
    while index_l < len(left) and index_r < len(right):
        if left[index_l] <= right[index_r]:
            result.append(left[index_l])
            index_l += 1
        else:
            result.append(right[index_r])
            index_r += 1

    while index_l < len(left):
        result.append(left[index_l])
        index_l += 1
    while index_r < len(right):
        result.append(right[index_r])
        index_r += 1
    return result

def merge_sort(sequence):
    # split the sequence into two till one left
    if len(sequence) == 1:
        return sequence
    else:
        length = len(sequence)
        index = (length // 2) + 1 if length % 2 else length // 2        
        left = merge_sort(sequence[:index])
        right = merge_sort(sequence[index:])
        return merge(left, right)


def main():
    x = [i for i in range(10, 0, -1)]
    print(x)
    print(merge_sort(x))


if __name__ == '__main__':
    main()