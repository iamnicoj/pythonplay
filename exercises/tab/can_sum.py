def can_sum_tab(target, numbers):
    if target == 0: return True

    dashboard = [[0 for _ in range(target + 1)] for _ in range(len(numbers))]

    for i in range(len(numbers)):
        # Create the seed 
        if numbers[i] <= target:
            dashboard[i][numbers[i]] = 1
            for number in numbers:             
                for j in range(target):
                    if (dashboard[i][j] == 1) and (j + number <= target):
                        dashboard[i][j + number ] = 1

            if dashboard[i][target] == 1: return dashboard

    return dashboard

print(can_sum_tab(0, [1, 2, 34])) # True.. OK
print(can_sum_tab(1, [2, 1, 34])) # True.. OK
print(can_sum_tab(1, [3, 2, 34])) # False.. OK
print(can_sum_tab(7, [2, 3, 8])) # True ERROR
print(can_sum_tab (8, [3, 5, 6, 7])) # True
print(can_sum_tab (8, [3, 6, 7])) # False


def can_sum_tab_optimized(target, numbers):
    dashboard = [0 for _ in range(target + 1)]

    dashboard[0] = 1

    for i in range(target + 1):
        for num in numbers:
            if (dashboard[i] > 0) and  (i + num < len(dashboard)):
                dashboard[i + num] += dashboard[i]
    
    return dashboard;

print('optimized: ')
print(can_sum_tab_optimized(0, [1, 2, 34])) # True.. OK
print(can_sum_tab_optimized(1, [2, 1, 34])) # True.. OK
print(can_sum_tab_optimized(1, [3, 2, 34])) # False.. OK
print(can_sum_tab_optimized(7, [2, 3, 8])) # True ERROR
print(can_sum_tab_optimized (8, [3, 5, 6, 7])) # True
print(can_sum_tab_optimized (8, [3, 6, 7])) # False

import copy

def how_sum_tab(target, numbers):
    dashboard = [[] for _ in range(target + 1)]

    dashboard[0] = [0]

    # for the best sum you keep a best result array
    # check for a better len with every match

    for i in range(target + 1):
        for num in numbers:
            if (len(dashboard[i]) > 0) and (i + num < len(dashboard)):
                extended_array = copy.deepcopy(dashboard[i])
                extended_array.extend([num])
                dashboard[i + num] = extended_array

                if (i + num) == target: 
                    return dashboard[target]
    
    return []

print('how sum: ')
print(how_sum_tab(0, [1, 2, 34])) # True.. OK
print(how_sum_tab(1, [2, 1, 34])) # True.. OK
print(how_sum_tab(1, [3, 2, 34])) # False.. OK
print(how_sum_tab(7, [2, 3, 8])) # True ERROR
print(how_sum_tab (8, [3, 5, 6, 7])) # True
print(how_sum_tab (8, [3, 6, 7])) # False


