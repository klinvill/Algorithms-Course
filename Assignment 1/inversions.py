__author__ = 'Kirby'
"""
This program was written for the week 1 assignment for the Algorithms: Design and Analysis, Part 1 course on Coursera
designed by Tim Roughgarden. It reads in a list of numbers from a text file and counts the number of inversions in the
list.

You can learn more about inversions here: https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)
You can find the Coursera course here: https://www.coursera.org/learn/algorithm-design-analysis
"""


def countCrossInversions(left, right):
    """
    Counts the number of cross inversions between two sorted lists
    :param left: sorted list
    :param right: sorted list
    :return: tuple of (merged sorted list, number of cross inversions)
    """
    inversions = 0
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))

        elif right[0] < left[0]:
            merged.append(right.pop(0))
            inversions += len(left)

        else:
            raise RuntimeError("This should never happen")



    if (len(left) > 0 and len(right) == 0):
        merged.extend(left)

    elif (len(right) > 0 and len(left) == 0):
        merged.extend(right)

    else:
        raise RuntimeError("This should never happen")

    return (merged, inversions)


def countInversions(nums):
    """
    counts the number of inversions in a list
    :param nums: list of numbers to count the inversions in
    :return: number of inversions in the list
    """
    return countInversionsHelper(nums)[1]



def countInversionsHelper(nums):
    """
    function that actually counts the number of inversions in a list. It also returns the sorted list so the
    countInversion function just wraps this function to provide the user with a more concise and logical interface.
    :param nums: list of numbers to count the inversions in
    :return: tuple of (sorted list, number of inversions in the list)
    """
    if len(nums) <= 1:
        return (nums, 0)

    halfpoint = int(len(nums)/2)
    left = nums[:halfpoint]
    right = nums[halfpoint:]

    left_sorted, left_inversions = countInversionsHelper(left)
    right_sorted, right_inversions = countInversionsHelper(right)
    merged, cross_inversions = countCrossInversions(left_sorted, right_sorted)

    return (merged, left_inversions+right_inversions+cross_inversions)



if __name__ == "__main__":
    with open('IntegerArray.txt', 'r') as f:
        ints = list(map(int, f.read().splitlines()))
        inversions = countInversions(ints)
        print("inversions: ", inversions)