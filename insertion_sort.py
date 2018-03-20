def insertion_sort(seq):
    for i in range(1, len(seq)):
        current = seq[i]
        while i > 0 and current < seq[i - 1]:
            # shift
            seq[i] = seq[i - 1]
            i -= 1
        seq[i] = current


def main():
    x = [i for i in range(10, 0, -1)]
    print(x)
    insertion_sort(x)
    print(x)


if __name__ == '__main__':
    main()
