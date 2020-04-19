def partitiontolist(partition):
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

def makeyoungdiag(partition):
    """
    Given a partition, return corresponding Young diagram implemented as a graph
    """
    diagram = {}
    parts_list = partitiontolist(partition)

    #loop for each part in partition
    for index in range(len(partition)):
        part = parts_list[index]
        part_length = partition[index]

        next_part = []
        if index + 1 < len(partition):
            next_part = parts_list[index + 1]
        part_length_next = len(next_part)

        #if not the last element in part, add descendant
        for k in range(part_length):
            diagram[part[k]] = set()
            #add descendant to right
            if k + 1 < part_length:
                diagram[part[k]].add(part[k+1])
            #add descendant below
            if k < part_length_next:
                diagram[part[k]].add(next_part[k])

    return diagram


def main():
    print("Enter a parition in decreasing order:")
    partition = [int(n) for n in input().split()]
    print("Partition:")
    print(partitiontolist(partition))
    ydiag = makeyoungdiag(partition)
    print("Corresponding Young diagram:")
    print(ydiag)

if __name__ == '__main__':
    main()
