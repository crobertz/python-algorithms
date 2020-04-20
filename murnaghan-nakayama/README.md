# murnaghan-nakayama

Python script implementing the recursive Murnaghan-Nakayama rule to compute character values of the symmetric group.

For details on algorithm, refer to <https://en.wikipedia.org/wiki/Murnaghan–Nakayama_rule>

Partitions are implemented using a list of nondecreasing integers.
All partitions are given in nonincreasing order.
For example the partition 3+2+1=6 corresponds to `[3, 2, 1]`.
As a string this partition corresponds to `'3 2 1'`.

`make_youngdiag` takes a partition string and returns the corresponding Young diagram implemented as a dictionary as follows:
Each box in the Young diagram is numbered along rows starting at the top-left box.
For example the Young diagram corresponding to the partition `[3, 2, 1]` will have numbering `1, 2, 3` in the first row, `4, 5` in the second row, and `6` in the last row.
Each Young diagram is then implemented as a dictionary whose keys are the numbers corresponding to the boxes and its value a dictionary of neighbours with keys `'r','l','d','u'` corresponding to the right, left, down, and up neighbour keys and `None` if no neighbours.
For example in the Young diagram corresponding to `[3, 2, 1]` the value of `5` is `{'r': None, 'l': 4, 'd': None, 'u': 2}`.

`character` takes two partitions `lambd` and `mu` given as lists of nonincreasing positive integers and returns the value of the character corresponding to `lambd` evaluated at `mu` using the recursive Murnaghan-Nakayama rule.
