def partitionlist(partition):
    """
    Given a partition of a positive integer n, returns list of lists where each element is an increasing list of integers.

    Example:
        partitionlist([3,2]) = [[1,2,3],[4,5]]
    """
    return_list = []
    current = 0
    for part in partition:
        part_list = [current + i for i in range(1,part+1)]
        current = part_list[-1]
        return_list.append(part_list)

    return return_list

def main():
    print("Enter a parition in decreasing order:")
    partition = [int(n) for n in input().split()]
    print(partitionlist(partition))

if __name__ == '__main__':
    main()
