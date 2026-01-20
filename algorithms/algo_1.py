
import heapq
import math


def most_largest_two(lst):
    max_first, max_second = sorted(lst[:2], reverse=True)
    for idx in range(2, len(lst)):
        if lst[idx] > max_first:
            max_first, max_second = lst[idx], max_first
        elif max_first >= lst[idx] >= max_second:
            max_second = lst[idx]
    return max_first, max_second


def heapq_two_largest(lst):
    lst_copy = lst[:]
    heapq.heapify(lst_copy)
    return heapq.nlargest(2, lst_copy)


def binary_search(ordered_lst, target):

    def bisect_innner(start, end):
        if start > end:
            return -1
        mid_idx = start + (end - start) // 2
        if target > ordered_lst[mid_idx]:
            return bisect_innner(mid_idx + 1, end)
        elif target < ordered_lst[mid_idx]:
            return bisect_innner(start, mid_idx - 1)
        else:
            return mid_idx
        
    return bisect_innner(0, len(ordered_lst) - 1)


# print(binary_search([2, 3, 7, 9, 13, 17, 19, 20], target=17))
# print(binary_search([2, 3, 7, 9, 13, 17, 19, 20], target=2))
# print(binary_search([2, 3, 7, 9, 13, 17, 19, 20], target=20))
# print(binary_search([2, 3, 7, 9, 13, 17, 19, 20], target=14))



def merge_sort(unsorted_lst):

    def merge(first_sublist, second_sublist):
        i = j = 0
        merged_lst = []
        while i < len(first_sublist) and j < len(second_sublist):
            if first_sublist[i] < second_sublist[j]:
                merged_lst.append(first_sublist[i])
                i += 1
            else:
                merged_lst.append(second_sublist[j])
                j += 1
        while i < len(first_sublist):
            merged_lst.append(first_sublist[i])
            i += 1
        while j < len(second_sublist):
            merged_lst.append(second_sublist[j])
            j += 1
        return merged_lst

    def divide(chaos_arr):
        if len(chaos_arr) == 1:
            return chaos_arr
        mid_idx = len(chaos_arr) // 2
        return merge(
            divide(chaos_arr[:mid_idx]), 
            divide(chaos_arr[mid_idx:])
        )
    
    return divide(unsorted_lst)


print(merge_sort([2, 7, 3, 5, 8, 1, 12]))


def jump_search(sorted_lst, target):
    
    def linear_search(start_idx, end_idx):
        for i in range(start_idx, end_idx + 1):
            if sorted_lst[i] == target:
                return i
        return -1
    
    def jump():
        block_size = int(math.sqrt(len(sorted_lst)))
        for i in range(0, len(sorted_lst) - block_size, block_size):
            if target == sorted_lst[i]:
                return i
            if sorted_lst[i] < target < sorted_lst[i + block_size]:
                return linear_search(i, i + block_size)
        else:
            return linear_search(i, len(sorted_lst) - 1)
    
    if len(sorted_lst) == 1:
        return 0 if sorted_lst[0] == target else -1
    elif len(sorted_lst) == 0:
        return -1
    else:
        return jump()


class Stack:

    def __init__(self) -> None:
        self._stack = list()
    
    def push(self, value):
        self._stack.append(value)
    
    def pop(self):
        return self._stack.pop()
    
    def peek(self):
        return self._stack[-1]
    
    def is_empty(self):
        return len(self._stack) == 0


def longest_valid_parenthese(string):
    """https://leetcode.com/problems/longest-valid-parentheses/"""
    counter = 0; stack = Stack()
    for cha in string:
        if cha == "(":
            stack.push(cha)
        if cha == ")" and not stack.is_empty() and stack.peek() == "(":
            stack.pop()
            counter += 2
    return counter


# print(longest_valid_parenthese("(()"))
# print(longest_valid_parenthese(")()())"))
# print(longest_valid_parenthese(""))
# print(longest_valid_parenthese(")((())()"))


def word_bank_two(string, word_dict):
    """https://leetcode.com/problems/word-break-ii/"""
    if len(string) == 0:
        return []
    for word in word_dict:
        if string.startswith(word):
            return [word] + word_bank_two(string[len(word):], word_dict)
    else:
        return 


# print(word_bank_two("catsanddog", word_dict=["cats", "cat", "and", "sand", "dog"]))


if __name__ == "__main__":
    # print(alternate([10, 2, 7, 3, 5, 8, 1, 12, 9]))
    # print(most_largest_two([13, 10, 2, 7, 12, 3, 5, 8, 1, 12, 9, 14]))
    # print(heapq_two_largest([14, 13, 10, 2, 7, 12, 3, 5, 8, 1, 12, 9, 14]))
    ...