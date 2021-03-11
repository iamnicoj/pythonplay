import copy

def can_construct(target, word_bank):
    return _can_construct(target, "", word_bank, {})

def _can_construct(target, concatenated, word_bank, memo):
    if memo.get(concatenated, None) is not None:
        return memo[concatenated]
    if target is None or target == "": 
        return False
    if target == concatenated: 
        return True
    if concatenated != "" and target.find(concatenated,0) != 0: 
        return False

    temp_concatenated = copy.deepcopy(concatenated)
    for word in word_bank:
        concatenated = temp_concatenated + word
        result = _can_construct(target, concatenated, word_bank, memo)
        memo[concatenated] = result
        if result: return True
    
    return False

# This algorithm can be implemented the other way around
# You can recursively check if each word is a prefix on the target
# then slice it out repitevely until you get an empty string and returnt True. False Otherwise


print(can_construct("",["as", "st", "te"])) # ?
print(can_construct("test",["as", "st", "t"])) # False
print(can_construct("test",["as", "st", "te"])) # True
print(can_construct("test",["as", "s", "e", "blue", "t"])) # True
print(can_construct("testinglikeakinginaworldofmuppets",["as", "s", "e", "blue", "t", "k", "o", "a", "i", "m", "u", "likeaking", "w"])) # False
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ['e',
            'ee',
            'eee',
            'eeee',
            'eeeee',
            'eeeeee',
            'eeeeeee',
            'eeeeeeee',
            'eeeeeeeee',
            'eeeeeeeeee',
            'eeeeeeeeeee',
            'eeeeeeeeeeee',
            'eeeeeeeeeeeee',
            'eeeeeeeeeeeeee',
            'eeeeeeeeeeeeeee',
            'eeeeeeeeeeeeeeee'
            ])) # False


def count_construct(target, word_bank):
    return _count_construct(target, word_bank, {})

def _count_construct(target, word_bank, memo):
    if memo.get(target) is not None: 
        return memo.get(target)
    if target == '':
        return 1
    
    temp_target = copy.deepcopy(target)
    result = 0
    for word in word_bank:
        if target.find(word, 0) == 0:
            second_temp_target = temp_target[slice(len(word), len(target))]
            result += _count_construct(second_temp_target, word_bank, memo)
    
    memo[target] = result
    return result




print('count_construct')
print(count_construct("",["as", "st", "te"])) # ?
print(count_construct("test",["as", "st", "t"])) # False
print(count_construct("test",["as", "st", "te"])) # True
print(count_construct("test",["as", "s", "e", "blue", "t"])) # True
print(count_construct("testinglikeakinginaworldofmuppets",["as", "s", "e", "blue", "t", "k", "o", "a", "i", "m", "u", "likeaking", "w"])) # False
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ['e',
            'ee',
            'eee',
            'eeee',
            'eeeee',
            'eeeeee',
            'eeeeeee',
            'eeeeeeee',
            'eeeeeeeee',
            'eeeeeeeeee',
            'eeeeeeeeeee',
            'eeeeeeeeeeee',
            'eeeeeeeeeeeee',
            'eeeeeeeeeeeeee',
            'eeeeeeeeeeeeeee',
            'eeeeeeeeeeeeeeee'
            ])) # False


def all_construct(target, word_bank):
    return _all_construct(target, word_bank, {})

def _all_construct(target, word_bank, memo):
    if target == '':
        return [[]]
    
    final_result = copy.deepcopy([]) # nope

    for word in word_bank:
        if target.find(word, 0 ) == 0:
            target_copy = copy.deepcopy(target)
            target_second_copy = copy.deepcopy(target_copy[slice(len(word), len(target))]) # nope

            parcial_result = _all_construct(target_second_copy, word_bank, memo)

            if len(parcial_result) > 0:
                for array in parcial_result:
                    added_word = copy.deepcopy([word])
                    added_word.extend(array)
                    final_result.append(copy.deepcopy(added_word))
    
    return final_result 
                
print('all_construct')
print(all_construct("",["as", "st", "te"])) # ?
print(all_construct("test",["as", "st", "t"])) # False
print(all_construct("test",["as", "st", "te", "e", "s", "t"])) # True
print(all_construct("test",["as", "s", "e", "blue", "t"])) # True
print(all_construct("testinglikeakinginaworldofmuppets",["as", "s", "e", "blue", "t", "k", "o", "a", "i", "m", "u", "likeaking", "w"])) # False
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ['e',
            'ee',
            'eee',
            'eeee',
            'eeeee',
            'eeeeee',
            'eeeeeee',
            'eeeeeeee',
            'eeeeeeeee',
            'eeeeeeeeee',
            'eeeeeeeeeee',
            'eeeeeeeeeeee',
            'eeeeeeeeeeeee',
            'eeeeeeeeeeeeee',
            'eeeeeeeeeeeeeee',
            'eeeeeeeeeeeeeeee'
            ])) # False
