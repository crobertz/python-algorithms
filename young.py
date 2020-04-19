import sys

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
    The value of each key is a dictionary whose value at keys 'r', 'd', 'l', 'u' are the right, down, left, up descendants respectively
    If there are no corresponding descendant then the value is None.
    """
    #add data of 'up' neighbour and 'left' neighbour?
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
        prev_part = []
        if index > 0:
            prev_part = parts_list[index - 1]

        #if not the last element in part, add descendant
        for k in range(part_length):
            diagram[part[k]] = {'r':None, 'd':None, 'l':None, 'u':None}
            #add descendant to right
            if k + 1 < part_length:
                diagram[part[k]]['r'] = part[k+1]
            #add descendant below
            if k < part_length_next:
                diagram[part[k]]['d'] = next_part[k]
            #add left parent
            if k > 0:
                diagram[part[k]]['l'] = part[k-1]
            if prev_part:
                diagram[part[k]]['u'] = prev_part[k]

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

def shape(ydiag):
    """
    Given a young diagram return its shape
    """
    if ydiag:
        return subshape(min(ydiag),ydiag)
    else:
        return []

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

def terminal(ydiag):
    """
    Given a young diagram, return list of terminal nodes (i.e. nodes with no right neighbour)
    """
    return [node for node in ydiag if not ydiag[node]['r']]

def delete_subdiag(box,ydiag):
    """
    Given a young diagram and a box, return a young diagram with the subdiagram starting at box deleted, with numbering respected from parent diagram
    """
    diagram = {}
    start_nodes = nodes_below(min(ydiag),ydiag)
    subdiagram = subdiag(box,ydiag)
    for node in start_nodes:
        current = node
        while current and not current in subdiagram:
            diagram[current] = {'r':None, 'd':None}
            #print(diagram)
            for key in diagram[current]:
                if not ydiag[current][key] in subdiagram:
                    diagram[current][key] = ydiag[current][key]
            current = ydiag[current]['r']

    return diagram

def skew_length(box,ydiag):
    """
    Given a young diagram and a box, returns length of longest skew diagram starting at box .
    The skew diagram travels downward whenever possible.
    """
    length = 0
    current = box
    while current:
        length += 1
        if ydiag[current]['d']:
            current = ydiag[current]['d']
        else:
            current = ydiag[current]['l']

    return length

def skew_lengths(box,ydiag):
    """
    Given a young diagram and a box, returns list of deletable skew lengths.
    The skew diagram travels downward whenever possible.
    """
    lengths = []
    length = 0
    current = box
    while current:
        length += 1
        if ydiag[current]['d']:
            current = ydiag[current]['d']
        else:
            lengths.append(length)
            current = ydiag[current]['l']

    return lengths

def delete_skew(box,length,ydiag):
    """
    Given a young diagram, delete a skew diagram starting at box and with given length.
    Skew diagrams travel down whenever possible.
    """

    diag = ydiag.copy()
    current = box

    for n in range(length):
        #print("loop count " + str(n))

        #update neighbours
        if diag[current]['u']:
            diag[diag[current]['u']]['d'] = None
        if diag[current]['l']:
            diag[diag[current]['l']]['r'] = None
        if diag[current]['d']:
            diag[diag[current]['d']]['u'] = None
        #print("current: " + str(current))
        #print(diag[current]['d'])
        #print(diag[current]['l'])

        #update current node. travel down whenever possible
        temp = current
        if diag[current]['d']:
            current = diag[current]['d']
            #print(current)
        else:
            current = diag[current]['l']
            #print(current)
        del diag[temp]

    return diag



#need a search for skew: start at terminal node and go left while going down whenever possible

def height(ydiag):
    """
    Given a young diagram returns its height
    """
    return len(nodes_below(min(ydiag),ydiag)) - 1

def character(lambd,rho):
    """
    Given two partitions lambd, rho, computes chi^lambd(rho) using recursive Murnaghan-Nakayama rule.
    """
    #check inputs
    sum1 = 0
    sum2 = 0
    for n in lambd:
        sum1 += n
    for n in rho:
        sum2 += n
    if sum1 != sum2:
        sys.exit("Need two partitions of same integer")

    #base case for recursion
    if len(lambd) == 0:
        return 1

    charval = 0

    #create young diagram corresponding to lambd
    diag = make_youngdiag(lambd)
    #print(shape(diag))

    # #populate subdiagram sizes
    # for node in diag:
    #     #diag[node]['subsize'] = subdiag_size(node,diag)
    #     if subdiag_size(node,diag) == rho[0]:
    #         #for each subdiagram with size equal to first entry of rho, delete subdiagram and recurse
    #         to_delete = subdiag(node,diag)
    #         deleted = delete_subdiag(node,diag)
    #         #print(to_delete)
    #         #print(shape(to_delete))
    #         #print(deleted)
    #         #print(shape(deleted))
    #         charval += ((-1)**height(to_delete))*character(shape(delete_subdiag(node,diag)),rho[1:])

    #for node in terminal(diag):

    #print(charval)
    #print(diag)
    return charval


def main():
    print("Enter a parition in decreasing order:")
    partition = [int(n) for n in input().split()]
    print("lambda = " + str(partition))
    print("Partition:")
    print(partition_to_list(partition))
    ydiag = make_youngdiag(partition)
    print("Shape:")
    print(shape(ydiag))
    print("Corresponding Young diagram:")
    print(ydiag)

    # print("Enter box to find skew diagram:")
    # box = int(input())
    # print("Skew length from box %d: %d" % (box, skew_length(box,ydiag)))

    print("Terminal skew lengths:")
    for n in terminal(ydiag):
        print("%d: %s" % (n,str(skew_lengths(n,ydiag)))
    print("Enter terminal to start deletion:")
    term = int(input())
    print("Enter length to delete:")
    del_length = int(input())
    print(delete_skew(term,del_length,ydiag))

    # print("Size of diagram: " + str(size(ydiag)))
    # print("Height of diagram: " + str(height(ydiag)))
    # print("Enter box to find subshape:")
    # n = int(input())
    # print("Shape of subdiagram starting at %d:" % n)
    # print(subshape(n,ydiag))
    # print("Size of subdiagram at %d: %d" % (n,subdiag_size(n,ydiag)))
    # print("Subdiagram:")
    # print(subdiag(n,ydiag))
    # print("Diagram with sub deleted:")
    # print(delete_subdiag(n,ydiag))
    # print("Shape of diagram with sub deleted:")
    # print(shape(delete_subdiag(n,ydiag)))

    # print("Enter another partition in decreasing order:")
    # partition2 = [int(n) for n in input().split()]
    # print("rho = " + str(partition2))
    # print("Character value: chi^lambda(rho) = " + str(character(partition,partition2)))

if __name__ == '__main__':
    main()
