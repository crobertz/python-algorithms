import sys
import copy

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

def terminal(ydiag):
    """
    Given a young diagram, return list of terminal nodes (i.e. nodes with no right neighbour)
    """
    return [node for node in ydiag if not ydiag[node]['r']]

def skew_lengths(box,ydiag):
    """
    Given a young diagram and a box, returns list of deletable skew lengths, where deletable length means upon deletion of given length diagram leaves a valid young diagram.
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
    Given a young diagram, delete a skew diagram starting at box and with given deletable length.
    Return new diagram with skew diagram deleted along with height of deleted skew diagram.
    Skew diagrams travel down whenever possible.
    """

    diag = copy.deepcopy(ydiag)
    current = box
    height = 0

    for n in range(length):
        #print("loop count " + str(n))

        #update neighbours
        if diag[current]['u']:
            diag[diag[current]['u']]['d'] = None
        if diag[current]['l']:
            diag[diag[current]['l']]['r'] = None
        if diag[current]['d']:
            diag[diag[current]['d']]['u'] = None

        #update current node. travel down whenever possible
        temp = current
        if diag[current]['d']:
            current = diag[current]['d']
            height += 1
        else:
            current = diag[current]['l']
        del diag[temp]

    return diag, height



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

    #recurse over deletable skew diagrams whose length is rho[0]
    for node in terminal(diag):
        if rho[0] in skew_lengths(node,diag):
            deleted, height = delete_skew(node,rho[0],diag)
            charval += ((-1)**height)*character(shape(deleted),rho[1:])

    return charval


def main():
    print("Enter a partition in decreasing order:")
    lambd = [int(n) for n in input().split()]
    print("lambda = " + str(lambd))
    ydiag = make_youngdiag(lambd)
    print("Enter another partition in decreasing order:")
    rho = [int(n) for n in input().split()]
    print("rho = " + str(rho))
    print("Character value: chi^lambda(rho) = " + str(character(lambd,rho)))

if __name__ == '__main__':
    main()
