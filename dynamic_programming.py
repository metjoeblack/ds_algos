
from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(6))
# print(fib(8))
# print(fib(12))
# print(fib(50))


def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        memo[n] = 1
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# print(fib_memo(6))
# print(fib_memo(8))
# print(fib_memo(12))
# print(fib_memo(150))


def fib_table(n):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21
    """
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1
    for i in range(n):
        table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]
    return table[n]


# print(fib_table(6))


def fib_table_v2(n):
    table = [None] * (n + 1)
    table[0], table[1] = 0, 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


# print(fib_table_v2(8))


@lru_cache(maxsize=256)
def grid_traverler_cache(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traverler_cache(m - 1, n) + grid_traverler_cache(m, n - 1)


# print(grid_traverler_cache(1, 1))
# print(grid_traverler_cache(2, 3))
# print(grid_traverler_cache(3, 2))
# print(grid_traverler_cache(3, 3))
# print(grid_traverler_cache(18, 18))



def grid_traveler(m, n):
    # grid_traveler(m, n) == grid_traveler(n, m)
    memo = {}

    def _helper(m, n):
        key = (m, n)  
        if key in memo:
            return memo[key]
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        memo[key] =  _helper(m - 1, n) + _helper(m, n - 1)
        return memo[key]

    return _helper(m, n)


# print(grid_traveler(1, 1))
# print(grid_traveler(2, 3))
# print(grid_traveler(3, 2))
# print(grid_traveler(3, 3))
# print(grid_traveler(18, 18))


def grid_traveler_table(m, n):
    table = [[0] * n for _ in range(m)]
    
    table[1][1] = 1

    for i in range(m):
        for j in range(n):
            current = table[i][j]
            if j + 1 < n:
                table[i][j + 1] += current
            if i + 1 < m:
                table[i + 1][j] += current
    print(table)
    
    # return table[m][n]


# print(grid_traveler_table(3, 3))


def grid_paths(n, m):
    memo = {}

    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1
    
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
    
    return memo[(n, m)]


# print(grid_paths(18, 18))


def can_sum(target_sum: int, numbers: list[int]) -> bool:

    @lru_cache(maxsize=None)
    def _helper(target_sum):
        if target_sum == 0:
            return True
        if target_sum < 0:
            return False
        for num in numbers:
            if _helper(target_sum - num):
                return True
        return False
    
    return _helper(target_sum)


# print(can_sum(7, [2, 3]))
# print(can_sum(7, [5, 3, 4, 7]))
# print(can_sum(7, [2, 4]))
# print(can_sum(8, [2, 3, 5]))
# print(can_sum(300, [7, 14]))



def can_sum_memo(target_sum: int, numbers: list[int]) -> bool:
    memo = {}

    def _helper(target_sum):
        if target_sum in memo:
            return memo[target_sum]
        if target_sum == 0:
            return True
        if target_sum < 0:
            return False
        for num in numbers:
            if _helper(target_sum - num):
                memo[target_sum] = True
                return True
        memo[target_sum] = False
        return False
    
    return _helper(target_sum)


# print(can_sum_memo(7, [2, 4]))
# print(can_sum_memo(8, [2, 3, 5]))
# print(can_sum_memo(300, [7, 14]))


def how_sum(target_sum, numbers):

    @lru_cache(maxsize=None)
    def _helper(target_sum):
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None
        
        for num in numbers:
            result = _helper(target_sum - num)
            if result is not None:
                return result + [num]
        
        return None
    
    return _helper(target_sum)


# print(how_sum(7, [2, 3]))
# print(how_sum(7, [5, 3, 4, 7]))
# print(how_sum(7, [2, 4]))
# print(how_sum(8, [2, 3, 5]))
# print(how_sum(300, [7, 14]))


def best_sum(target_sum, numbers):
    memo = {}

    def _helper(target_sum):
        if target_sum in memo:
            return memo[target_sum]
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None
        
        shortest_combination = None

        for num in numbers:
            ret = _helper(target_sum - num)
            if ret is not None:
                combination = ret + [num]
                if (
                    shortest_combination is None or 
                    len(combination) < len(shortest_combination)
                ):
                    shortest_combination = combination

        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return _helper(target_sum)


# print(best_sum(7, [5, 3, 4, 7]))
# print(best_sum(8, [2, 3, 5]))
# print(best_sum(8, [1, 4, 5]))
# print(best_sum(100, [1, 2, 5, 25]))



def best_sum_cache(target_sum, numbers):

    @lru_cache(maxsize=None)
    def _helper(target_sum):
        if target_sum == 0:
            return []
        if target_sum < 0:
            return None
        
        shortest_combination = None

        for num in numbers:
            ret = _helper(target_sum - num)
            if ret is not None:
                combination = ret + [num]
                if (
                    shortest_combination is None or 
                    len(combination) < len(shortest_combination)
                ):
                    shortest_combination = combination
        
        return shortest_combination

    return _helper(target_sum)


# print(best_sum_cache(7, [5, 3, 4, 7]))
# print(best_sum_cache(8, [2, 3, 5]))
# print(best_sum_cache(8, [1, 4, 5]))
# print(best_sum_cache(100, [1, 2, 5, 25]))



def can_construct(original_str, word_bank):
    
    @lru_cache(maxsize=None)
    def _helper(original_str):
        if original_str == "":
            return True
        for word in word_bank:
            if original_str.startswith(word):
                suffix = original_str[len(word):]
                if _helper(suffix):
                    return True
        return False
    
    return _helper(original_str)


# print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct(
#     "skateboard", 
#     ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
# ))
# print(can_construct(
#     "enterapotentpot", 
#     ["a", "p", "ent", "enter", "ot", "o", "t"]
# ))
# print(can_construct(
#     "eeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
#     ["e", "ee", "eee", "eeeeeee", "eeeeeeeee"]
# ))


def can_construct_memo(original_str, word_bank):
    memo = {}
    
    def _helper(original_str):
        if original_str in memo:
            return memo[original_str]
        if original_str == "":
            return True
        
        for word in word_bank:
            if original_str.startswith(word):
                suffix = original_str[len(word):]
                if _helper(suffix):
                    memo[original_str] = True
                    return True
                
        memo[original_str] = False
        return False
    
    return _helper(original_str)


# print(can_construct_memo("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct_memo(
#     "skateboard", 
#     ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
# ))
# print(can_construct_memo(
#     "enterapotentpot", 
#     ["a", "p", "ent", "enter", "ot", "o", "t"]
# ))
# print(can_construct_memo(
#     "eeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
#     ["e", "ee", "eee", "eeeeeee", "eeeeeeeee"]
# ))



def count_construct(target, words_bank):

    @lru_cache(maxsize=None)
    def _helper(target):
        if target == "":
            return 1
        
        total_count = 0
        
        for word in words_bank:
            if target.startswith(word):
                total_count += _helper(target[len(word):])
        
        return total_count
    
    return _helper(target)


# print(count_construct(
#     "purple",
#     ["purp", "p", "ur", "le", "purpl"]
# ))
# print(count_construct(
#     "abcdef",
#     ["ab", "abc", "cd", "def", "abcd"]
# ))
# print(count_construct(
#     "skateboard",
#     ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
# ))
# print(count_construct(
#     "enterapotentpot",
#     ["a", "p", "ent", "enter", "ot", "o", "t"]
# ))
# print(count_construct(
#     "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#     ["e", "ee", "eee", "eeee", "eeeeeeee"]
# ))


def all_construct(target, word_bank):
    # memo = {}
    @lru_cache(maxsize=None)
    def _helper(target):
        # if target in memo:
        #     return memo[target]
        if target == "":
            return [[]]
        
        result = []

        for word in word_bank:
            if target.startswith(word):
                suffix_ways = _helper(target[len(word):])
                target_ways =  [[word] + item for item in suffix_ways]
                result += target_ways
        
        # memo[target] = result
        return result

    return _helper(target)


# print(all_construct(
#     "purple",
#     ["purp", "p", "ur", "le", "purpl"]
# ))
# print(all_construct(
#     "abcdef",
#     ["ab", "abc", "cd", "def", "abcd", "ef", "c"]
# ))
# print(all_construct(
#     "skateboard",
#     ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
# ))


@lru_cache(maxsize=None)
def decode_ways(digit_str: str) -> list:
    """
    https://leetcode.com/problems/decode-ways/
    '11106' --> [[1, 1, 10, 6], [11, 10, 6]]
    """
    if digit_str == "":
        return [[]]
    result = []
    if not digit_str.startswith("0"):
        if len(digit_str) >= 2 and int(digit_str[:2]) <= 26:
            ret = decode_ways(digit_str[2:])
            result += [[digit_str[:2]] + sub for sub in ret]
        ret = decode_ways(digit_str[1:])
        result += [[digit_str[0]] + sub for sub in ret]
    return result


# print(decode_ways("11106"))
# print(decode_ways("12"))
# print(decode_ways("226"))
# print(decode_ways("06"))
# print(decode_ways("123"))
# print(decode_ways("1221"))


def make_changes(changes, coins):
    
    @lru_cache(maxsize=None)
    def _helper(changes):
        if changes == 0:
            return [[]]
        if changes < 0:
            return None
        result = []
        for coin in coins:
            ret = _helper(changes - coin)
            if ret is not None:
                result += [sub + [coin] for sub in ret]
        return result
    return _helper(changes)


# print(make_changes(9, [2, 3, 5]))


def make_min_changes(changes, coins):
    
    @lru_cache(maxsize=None)
    def _helper(changes):
        if changes == 0:
            return []
        if changes < 0:
            return None
        shortest_changes = None
        for coin in coins:
            ret = _helper(changes - coin)
            if ret is not None:
                result = ret + [coin]
                if (
                    shortest_changes is None or
                    len(result) < len(shortest_changes)
                ):
                    shortest_changes = result
        return shortest_changes
    return _helper(changes)


# print(make_min_changes(13, [1, 2, 5]))
# print(make_min_changes(100, [1, 2, 5, 25]))


def rod_cutting_problem(rod_length, length_lst, prices_lst):
    """
    https://www.techiedelight.com/rod-cutting/
    """
    lp_map = dict(zip(length_lst, prices_lst))
    
    @lru_cache(maxsize=None)
    def _helper(rod_length):
        if rod_length == 0:
            return 0
        max_profit = None
        for length in length_lst:
            if rod_length >= length:
                profit = lp_map[length] + _helper(rod_length - length)
                if max_profit is None or profit > max_profit:
                    max_profit = profit
        return max_profit
    
    return _helper(rod_length)


# print(rod_cutting_problem(
#     4,
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 5, 8, 9, 10, 17, 17, 20]
# ))


def countStrings(n, last_digit=0):
    """
    https://www.techiedelight.com/find-n-digit-binary-strings-without-consecutive-1s/
    """
    if n == 0:
        return 0
    if n == 1:
        return 1 if last_digit == 1 else 2
    
    if last_digit == 0:
        return countStrings(n - 1, 1) + countStrings(n - 1, 0)
    else:
        return countStrings(n - 1, 0)


# print(countStrings(5))


def is_interleaving(s, x, y):
    """
    https://www.techiedelight.com/check-string-interleaving-two-given-strings/
    """
    if not (s or x or y):
        return True
    
    if x and x[0] == s[0]:
        if is_interleaving(s[1:], x[1:], y):
            return True
    
    if y and y[0] == s[0]:
        if is_interleaving(s[1:], x, y[1:]):
            return True
    
    return False


# print(is_interleaving("ACABDC", "ABC", "ACD"))
# print(is_interleaving("ACDB", "AB", "CD"))
# print(is_interleaving("ADBECF", "ABC", "DEF"))
# print(is_interleaving("AACBCD", "ABC", "ACD"))
# print(is_interleaving("AACCBD", "ABC", "ACD"))
# print(is_interleaving("ACDABC", "ABC", "ACD"))



if __name__ == "__main__":
    pass
