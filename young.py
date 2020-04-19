def partition_to_list(partition):
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

def make_youngdiag(partition):
    """
    Given a partition, return corresponding Young diagram implemented as a graph

    Each Young diagram is a dictionary,
    The value of each key is a dictionary whose value at key 'r' is the right descendant while the value at key 'd' is the down descendant.
    If there are no corresponding descendant then the value is None.
    """
    diagram = {}
    parts_list = partition_to_list(partition)

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
            diagram[part[k]] = {'r':None, 'd':None}
            #add descendant to right
            if k + 1 < part_length:
                diagram[part[k]]['r'] = part[k+1]
            #add descendant below
            if k < part_length_next:
                diagram[part[k]]['d'] = next_part[k]

    return diagram

def nodes_below(box,ydiag):
    """
    Given a young diagram and a box, return list of nodes below and including box
    """
    current = box
    nodes = []
    while current:
        nodes.append(current)
        current = ydiag[current]['d']

    return nodes

def subshape(box,ydiag):
    """
    Given a young diagram and box in the diagram, returns shape of subdiagram whose top left corner starts at box
    """

    left_nodes = nodes_below(box,ydiag)
    subshape = []
    #iterate over rows of subdiagram
    for node in left_nodes:
        shape = 1
        current = node
        while ydiag[current]['r']:
            current = ydiag[current]['r']
            shape += 1
        subshape.append(shape)

    return subshape

def subdiag_size(box,ydiag):
    """
    Given a young diagram and box in the diagram, returns size of subdiagram whose top left corner starts at box
    """

    shape = subshape(box,ydiag)
    size = 0
    for n in shape:
        size += n
    return size

def size(ydiag):
    """
    Return size of diagram
    """
    return subdiag_size(1,ydiag)

def subdiag(box,ydiag):
    """
    Given a box and a young diagram, return subdiagram starting at box with node numberings inherited from parent
    """
    subdiag = {}
    start_nodes = nodes_below(box,ydiag)
    #iterate over rows to add nodes
    for node in start_nodes:
        current = node
        while current:
            subdiag[current] = ydiag[current]
            current = ydiag[current]['r']

    return subdiag

def delete_subdiag(box,ydiag):
    """
    Given a young diagram and a box, return a young diagram with the subdiagram starting at box deleted, with numbering respected from parent diagram
    """
    diagram = {}
    start_nodes = nodes_below(1,ydiag)
    subdiagram = subdiag(box,ydiag)
    for node in start_nodes:
        current = node
        while not current in subdiagram:
            diagram[current] = {'r':None, 'd':None}
            for key in diagram[current]:
                if not ydiag[current][key] in subdiagram:
                    diagram[current][key] = ydiag[current][key]
            current = ydiag[current]['r']

    return diagram



def main():
    print("Enter a parition in decreasing order:")
    partition = [int(n) for n in input().split()]
    print("Partition:")
    print(partition_to_list(partition))
    ydiag = make_youngdiag(partition)
    print("Corresponding Young diagram:")
    print(ydiag)
    print("Size of diagram: " + str(size(ydiag)))
    print("Enter box to find subshape:")
    n = int(input())
    print("Shape of subdiagram starting at %d:" % n)
    print(subshape(n,ydiag))
    print("Size of subdiagram at %d: %d" % (n,subdiag_size(n,ydiag)))
    print("Subdiagram:")
    print(subdiag(n,ydiag))
    print("Diagram with sub deleted:")
    print(delete_subdiag(n,ydiag))

if __name__ == '__main__':
    main()
