from collections import Counter


def identifyPermutation(first_str, second_str):
    if len(first_str) != len(second_str):
        return False
    first_str = [_ for _ in first_str]
    chr = 0
    while chr < len(second_str):
        if first_str[chr] in second_str:
            chr += 1
            continue
        else:
            return False
    return True


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


def comBySort(str1, str2):
    j = 0
    counterStr2 = sorted(str2)
    counterStr1 = sorted(str1)
   # print("first",counterStr1)
   # print("second",counterStr2)
    for i in str2:
        if counterStr2[j] == counterStr1[j]:
            j += 1
            continue
        else:
            return False
    return True


str1 = "savinirs"  # have given srinivas in reverse
str2 = "ssrinvai"

print("strings comparison by trail method - many times wrong:-",
      identifyPermutation(str1, str2))  # yeilds wrong result

print("strings comparison by counter method:-",
      check_permutation(str1, str2))  # correct algo

print("strings comparison by sort method:-",
      comBySort(str1, str2))  # compare by sorting
