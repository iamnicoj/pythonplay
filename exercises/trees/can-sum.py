def can_sum(target, numarray):
    result = []
    _can_sum(target, numarray, result, {})

    return result

def _can_sum(target, numarray, path, memo={}):
    if memo.get(target, None) is not None: 
        return memo[target]
    if target == 0: 
        return True
    if target < 0: 
        return False
    if 1 in numarray: 
        return True

    for num in numarray:
        result = _can_sum(target - num, numarray, path, memo);
        if result == True: 
            path.append(num)
            break
    
    memo[target] = result
    return result

# print(can_sum(0,[1])) # True
# print(can_sum(1,[1])) # True //TODO shouldn't be an empty array
# print(can_sum(7,[3,4,8])) # True
# print(can_sum(2,[3, 4])) # False
# print(can_sum(3000, [17, 21, 7, 31, 23])) # True
# print(can_sum(3001, [19, 3004, 3000, 2500, 1000, 1509])) # False

def any_sum_v2(target, numarray):
    return _any_sum_v2(target, numarray, {})


# No boolean just list management
def _any_sum_v2(target, numarray, memo={}):
    if memo.get(target, None) is not None: 
        return memo[target]
    if target == 0: 
        return []
    if target < 0: 
        return None
    if 1 in numarray: 
        return [1 for _ in range(target)]

    for num in numarray:
        result = _any_sum_v2(target - num, numarray, memo);
        if result is not None: 
            result.extend([num])
            break
    
    memo[target] = result
    return result

# print(any_sum_v2(0,[1])) # True
# print(any_sum_v2(1,[1])) # True //TODO shouldn't be an empty array
# print(any_sum_v2(7,[3,4,8])) # True
# print(any_sum_v2(2,[3, 4])) # False
# print(any_sum_v2(3000, [17, 21, 7, 31, 23])) # True
# print(any_sum_v2(3001, [19, 3004, 2500, 1000, 1001, 1509, 3001])) # False


import copy

def best_sum_v2(target, numarray):
    # the next line won't affect the result in any way
    return _best_sum_v2(target, numarray, {})

# No boolean just list management
def _best_sum_v2(target, numarray, memo={}):
    if memo.get(target, -1) != -1: 
        return memo[target]
    if target == 0: 
        return []
    if target < 0: 
        return None

    shortest = None
    reminder_combination = None

    for num in numarray:
        # this is probably the most important line of code from the day. 
        # when modifying list of objects from python in a recursive call
        # MAKE A FUKING DEEP COPY
        reminder_combination = copy.deepcopy(_best_sum_v2(target - num, numarray, memo))
        if reminder_combination is not None: 
            reminder_combination.extend([num])
            if shortest is None or len(reminder_combination) < len(shortest):
                shortest = reminder_combination
    
    memo[target] = copy.deepcopy(shortest)
    return shortest

print(best_sum_v2(0,[1])) # True
print(best_sum_v2(1,[1])) # True //TODO shouldn't be an empty array
print(best_sum_v2(7,[3,4,8])) # True
print(best_sum_v2(2,[3, 4])) # False
print(best_sum_v2(8, [2, 3, 5]))
print(best_sum_v2(100,[1,2,5,25]))
print(best_sum_v2(3000, [17, 21, 7, 31, 23])) # True
print(best_sum_v2(3001, [19, 3004, 2500, 1000, 1001, 1509, 3001])) # False
