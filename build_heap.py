# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2 -1, -1, -1):
        swaps+= sift_down(data,i)
    return swaps

def sift_down(data,i):
    swaps = []
    n = len(data)
    left = 2*i + 1
    right = 2*i + 2
    min_index = i
    if left < n and data[left] < data[min_index]:
        min_index = left
    if right < n and data[right] < data[min_index]:
        min_index = right
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        swaps += sift_down(data, min_index)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    assert len(swaps) <= 4*n
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
