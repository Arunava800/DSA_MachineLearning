"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of
the puzzle is to move all the disks from source rod to destination rod using the third rod
(say auxiliary rod). The rules are:
1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of the rod
3. No disk can be placed on top of a smaller disk
Print the steps required to move `n` disks from source rod to destination rod. Source rod is
named as `a`, auxiliary rod as `b` and destination rod as `c`
"""


def tower_of_hanoi(n, source, aux, des):
    if n == 1:
        print(source, des)
        return
    tower_of_hanoi(n-1, source, des, aux)
    print(source, des)
    tower_of_hanoi(n-1, aux, source, des)


def tower_of_hanoi_copy(n, source, aux, des):
    if n > 0:
        tower_of_hanoi(n-1, source, des, aux)
        print(source, des)
        tower_of_hanoi(n-1, aux, source, des)


num_disk = int(input())
tower_of_hanoi(num_disk, 'a', 'b', 'c')
tower_of_hanoi_copy(num_disk, 'a', 'b', 'c')
