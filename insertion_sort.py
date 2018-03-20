import random


def insertion_sort(seq):
    for i in range(1, len(seq)):
        while i > 0 and seq[i] < seq[i - 1]:
            # swap
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1


def main():
    r = random.SystemRandom()
    x = [i for i in range(10, 0, -1)]
    r.shuffle(x)
    print(x)
    insertion_sort(x)
    print(x)


if __name__ == '__main__':
    main()
