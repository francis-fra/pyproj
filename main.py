import sys
from problems.solution import nonDivisibleSubset

def test_case_01():
    lst = [19, 10, 12, 24, 25, 22]
    k = 4
    ans = nonDivisibleSubset(k, lst)
    print(ans)

def test_case_02():
    lst = [1, 7, 2, 4]
    k = 3
    ans = nonDivisibleSubset(k, lst)
    print(ans)

def test_case_03():
    lst = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
    k = 7
    ans = nonDivisibleSubset(k, lst)
    print(ans)

def main():
    test_case_01()
    # test_case_02()
    # test_case_03()


main()